# Authentication

This documentation uses the GitHub REST API with **Personal Access Token (PAT)** authentication.

GitHub authenticates requests using the `Authorization` header:

- Header: `Authorization`
- Scheme: `Bearer`
- Value: your personal access token

Example:

```http
Authorization: Bearer <TOKEN>
