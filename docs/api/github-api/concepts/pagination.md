# Pagination

Many GitHub REST API endpoints return large result sets. To keep responses fast and predictable, GitHub paginates responses.

This documentation uses **cursor-based pagination** via the `Link` response header.

---

## Query parameters

Common pagination parameters include:

| Parameter | Type | Description |
|---|---|---|
| `per_page` | integer | Number of items per page (default varies by endpoint). |
| `page` | integer | Page number to request. |

Example (request 5 repositories per page):

```powershell
curl.exe -i -H "Authorization: Bearer $env:GITHUB_TOKEN" `
  -H "X-GitHub-Api-Version: 2022-11-28" `
  "https://api.github.com/user/repos?per_page=5"

When tested against the `/user/repos` endpoint, the response did not
include a `Link` header because the authenticated user had fewer results
than the requested `per_page` value.

GitHub only returns pagination links when additional pages are available.
