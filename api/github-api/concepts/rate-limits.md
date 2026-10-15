# Rate limits

GitHub REST API requests are subject to rate limits. If you exceed a limit, requests may fail until the limit resets.

Rate limiting helps protect the API from abuse and ensures fair usage across clients.

---

## Rate limit headers

Many responses include headers that describe your current rate limit status:

| Header | Meaning |
|--------|---------|
| `X-RateLimit-Limit` | Total number of requests allowed in the current window. |
| `X-RateLimit-Remaining` | Requests remaining before you are rate limited. |
| `X-RateLimit-Reset` | Time when the limit resets (Unix epoch seconds). |
| `X-RateLimit-Used` | Requests used in the current window (may not appear on every endpoint). |
| `X-RateLimit-Resource` | The limit bucket being applied (may not appear on every endpoint). |

---

## How to check your current limit

You can inspect rate limit headers by requesting headers only.

```powershell
curl.exe -I -H "Authorization: Bearer $env:GITHUB_TOKEN" `
  -H "X-GitHub-Api-Version: 2022-11-28" `
  "https://api.github.com/user"
```

## A typical response includes values like:

X-RateLimit-Limit: 5000

X-RateLimit-Remaining: 4992

X-RateLimit-Reset: 1767720920

## What happens when you hit the limit

If you exceed the applicable limit, the API may return:

* 403 Forbidden with messaging indicating rate limiting.

When handling rate limits in scripts or integrations:

* Reduce request frequency (backoff)

* Cache responses when appropriate

* Retry after the reset time indicated by X-RateLimit-Reset
