# List repositories for the authenticated user

Returns repositories that the authenticated user has explicit permission to access.

---

## Request

**Method:** `GET`  
**Path:** `/user/repos`  
**Full URL:** `https://api.github.com/user/repos`

---

## Headers

| Header | Required | Description |
|------|----------|-------------|
| `Authorization: Bearer <TOKEN>` | Yes | Personal access token used to authenticate the request. |
| `X-GitHub-Api-Version: 2022-11-28` | Recommended | Locks API behavior to a specific version. |

---

## Query parameters

| Parameter | Type | Required | Description |
|----------|------|----------|-------------|
| `per_page` | integer | No | Number of results per page. |
| `page` | integer | No | Page number to return. |
| `sort` | string | No | Sort order (for example: `created`, `updated`, `pushed`, `full_name`). |
| `direction` | string | No | Sort direction: `asc` or `desc`. |

> Pagination details: see [`concepts/pagination.md`](../concepts/pagination.md).

---

## Example request (PowerShell)

```powershell
curl.exe -i -H "Authorization: Bearer $env:GITHUB_TOKEN" `
  -H "X-GitHub-Api-Version: 2022-11-28" `
  "https://api.github.com/user/repos?per_page=5&sort=updated"
```

## Example response 
```
[
  {
    "id": 123,
    "name": "developer-platform-docs",
    "full_name": "SantiUlibarri/developer-platform-docs",
    "private": false,
    "html_url": "https://github.com/SantiUlibarri/developer-platform-docs"
  }
]
```
## Errors

| Status code | Meaning      | Description                                                                            |
| ----------- | ------------ | -------------------------------------------------------------------------------------- |
| 401         | Unauthorized | The request is missing a valid authentication token.                                   |
| 403         | Forbidden    | The token is valid but lacks required permissions or the rate limit has been exceeded. |


