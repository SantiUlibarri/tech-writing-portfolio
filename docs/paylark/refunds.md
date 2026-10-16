# Refund an order
 
Use `POST /orders/{order_id}/refunds` to return all or part of a payment to the customer. You can only refund orders whose status is `completed`.
 
## Before you begin
 
You need:
 
- Your Paylark test API key. It starts with `sk_test_`. If you don't have one yet, start with the [Quickstart](quickstart.md).
- An order with the status `completed`. You can only refund orders that were paid.
- The order's `order_id`, the reference you chose when you created the order.
## Refund the full amount
 
Send an empty JSON object. Without an `amount`, Paylark refunds everything that hasn't been refunded yet.
 
=== "curl"
 
```bash
    curl -X POST https://api.test.paylark.example/v1/orders/shop-10045/refunds \
      -H "Authorization: Bearer $PAYLARK_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{}'
```
 
=== "PowerShell"
 
```powershell
    Invoke-RestMethod -Method Post `
        -Uri "https://api.test.paylark.example/v1/orders/shop-10045/refunds" `
        -Headers @{ Authorization = "Bearer $env:PAYLARK_API_KEY" } `
        -ContentType "application/json" -Body "{}"
```
 
Paylark responds with `201 Created` and the refund:
 
```json
{
  "id": "ref_8Mf2WqT5",
  "order_id": "shop-10045",
  "amount": 4995,
  "currency": "EUR",
  "status": "completed",
  "created_at": "2026-10-16T09:12:44Z"
}
```
 
The order's status changes to `refunded`.
 
## Refund part of the amount
 
Send the `amount` to refund. You can also add a `reason`, which is an internal note that the customer doesn't see.
 
=== "curl"
 
```bash
    curl -X POST https://api.test.paylark.example/v1/orders/shop-10045/refunds \
      -H "Authorization: Bearer $PAYLARK_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "amount": 2000,
        "reason": "Customer returned one item"
      }'
```
 
=== "PowerShell"
 
```powershell
    $body = @{ amount = 2000; reason = "Customer returned one item" } | ConvertTo-Json
 
    Invoke-RestMethod -Method Post `
        -Uri "https://api.test.paylark.example/v1/orders/shop-10045/refunds" `
        -Headers @{ Authorization = "Bearer $env:PAYLARK_API_KEY" } `
        -ContentType "application/json" -Body $body
```
 
!!! info "Amounts are in cents"
    `amount` is an integer in the currency's smallest unit. `2000` refunds €20.00.
 
Paylark responds with `201 Created`:
 
```json
{
  "id": "ref_3Kd9LpQ2",
  "order_id": "shop-10045",
  "amount": 2000,
  "currency": "EUR",
  "status": "completed",
  "reason": "Customer returned one item",
  "created_at": "2026-10-16T09:12:44Z"
}
```
 
You can issue several partial refunds, as long as their total doesn't exceed the order amount. After a partial refund, the order stays `completed` and its `amount_refunded` field shows the total refunded so far. When `amount_refunded` reaches `amount`, the status changes to `refunded`.
 
## Track the refund
 
Every refund has its own `status`:
 
| Refund status | Meaning | What to do |
|---|---|---|
| `pending` | Paylark is processing the refund. | Check again later with [Get an order](reference/index.md). |
| `completed` | The refund was sent to the customer's original payment method. | Nothing. Update the order in your system. |
| `failed` | The refund couldn't be sent, for example because the customer's card was closed. | Contact Paylark support with the refund `id`. |
 
How long the money takes to reach the customer depends on their bank and payment method.
 
!!! warning "Partial refunds don't trigger a webhook"
    Paylark sends an `order.status_changed` webhook only when the order's status changes. A full refund changes the status to `refunded`, so you get a webhook. A partial refund leaves the status as `completed`, so no webhook is sent. To confirm a partial refund, use the `201` response or call [Get an order](reference/index.md) and check `amount_refunded`.
 
## Errors
 
| Status | `code` | Meaning | What to do |
|---|---|---|---|
| `401` | `missing_api_key` or `invalid_api_key` | The API key is missing, invalid, or for the wrong environment. | Check the `Authorization` header and that you're using a test key with the test base URL. |
| `404` | `order_not_found` | No order exists with this `order_id`. | Check the `order_id` and the environment. Test and live orders are separate. |
| `409` | `order_not_refundable` | The order isn't `completed`. | Check the order's status. Only paid orders can be refunded. See [Payment statuses](payment-statuses.md). |
| `422` | `refund_exceeds_balance` | The `amount` is more than what's left to refund. | Get the order, subtract `amount_refunded` from `amount`, and refund at most that. |
| `429` | `rate_limited` | Too many requests. | Wait for the number of seconds in the `Retry-After` header, then retry. |
 
Every error includes a `request_id`. Include it when you contact Paylark support.
 
## Testing refunds
 
You can try every request on this page against the Paylark mock server, without a test account:
 
1. Start the mock server from the repository root:
```bash
    npx @stoplight/prism-cli mock docs/paylark/openapi.yaml
```
 
2. In the examples above, replace `https://api.test.paylark.example/v1` with `http://127.0.0.1:4010`.
3. To see an error response, add a `Prefer` header with the status code:
```bash
    curl -X POST http://127.0.0.1:4010/orders/shop-10045/refunds \
      -H "Authorization: Bearer sk_test_portfolio" \
      -H "Content-Type: application/json" \
      -H "Prefer: code=409" \
      -d '{}'
```
 
The mock server returns the examples from the [OpenAPI specification](openapi.yaml), so every successful refund returns the same example response.
 
