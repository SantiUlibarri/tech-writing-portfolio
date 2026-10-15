# Paylark Payments API

The Paylark Payments API lets merchants accept online payments through a hosted payment page, track each order through its payment lifecycle, and refund completed payments.

!!! info "About this sample"
    Paylark is a fictional payment service provider (PSP), created for this portfolio. Its design follows common PSP conventions: a redirect flow, order statuses, signed webhooks, and separate test and live environments. Using a fictional API let me build the full documentation toolchain end to end: the OpenAPI specification, the generated reference, a mock server, and a Postman collection.

## Environments

| Environment | Base URL | API keys start with |
|---|---|---|
| Test | `https://api.test.paylark.example/v1` | `sk_test_` |
| Live | `https://api.paylark.example/v1` | `sk_live_` |

Test keys work only in the test environment, and live keys only in the live environment.

## Where to start

- **[API reference](reference/index.md)**: every endpoint, request field, response, and error, generated from the [OpenAPI specification](openapi.yaml).