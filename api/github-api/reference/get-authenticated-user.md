# Get the authenticated user

Returns profile information for the authenticated GitHub user.

---

## Request

**Method:** `GET`  
**Path:** `/user`  
**Full URL:** `https://api.github.com/user`

---

## Headers

| Header | Required | Description |
|------|----------|-------------|
| `Authorization: Bearer <TOKEN>` | Yes | Personal access token used to authenticate the request. |
| `X-GitHub-Api-Version: 2022-11-28` | Recommended | Locks API behavior to a specific version. |

---

## Example request (PowerShell)

```powershell
curl.exe -H "Authorization: Bearer $env:GITHUB_TOKEN" `
  -H "X-GitHub-Api-Version: 2022-11-28" `
  https://api.github.com/user
```
## Example response
```
{
  "login": "SantiUlibarri",
  "id": 251346436,
  "type": "User",
  "site_admin": false,
  "name": "Santiago Fernandez Ulibarri",
  "location": "Madrid"
}
```
## Errors

| Status code | Meaning      | Description                                                                            |
| ----------- | ------------ | -------------------------------------------------------------------------------------- |
| 401         | Unauthorized | The request is missing a valid authentication token.                                   |
| 403         | Forbidden    | The token is valid but lacks required permissions or the rate limit has been exceeded. |

