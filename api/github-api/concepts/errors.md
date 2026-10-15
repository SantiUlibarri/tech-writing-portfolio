# Errors

GitHub REST API errors are communicated using standard HTTP status codes and a JSON response body.

This documentation uses a consistent approach to help developers quickly understand:
- what failed
- why it failed
- how to fix it

---

## Common status codes

| Status code | Meaning | Typical cause |
|------------|---------|---------------|
| 400 | Bad Request | Invalid request syntax or unsupported parameters. |
| 401 | Unauthorized | Missing, invalid, or expired token. |
| 403 | Forbidden | Token lacks permission **or** you are rate limited. |
| 404 | Not Found | Resource does not exist **or** is not accessible to the token. |
| 422 | Unprocessable Entity | Validation failed (common on write operations). |

---

## Error response body

Many GitHub API errors return a JSON body with fields such as:

- `message`: human-readable explanation
- `documentation_url`: link to GitHub documentation
- `errors`: optional array with more detail (common on validation failures)

Example:

```json
{
  "message": "Bad credentials",
  "documentation_url": "https://docs.github.com/rest"
}
```
Error payloads vary by endpoint. Always check the status code and message.

## Troubleshooting workflow

Use this quick flow when diagnosing failures:

1. **Check the status code**
   - `401` → authentication problem
   - `403` → permission issue or rate limit exceeded
   - `404` → wrong path/identifier or insufficient access

2. **Check required headers**
   - `Authorization`
   - `X-GitHub-Api-Version`

3. **Check rate limit headers**
   - `X-RateLimit-Remaining`
   - `X-RateLimit-Reset`

4. **Retry safely**
   - Only retry idempotent requests (`GET`) automatically
   - For write operations (`POST`, `PUT`, `PATCH`, `DELETE`), confirm whether the request may have partially succeeded before retrying
