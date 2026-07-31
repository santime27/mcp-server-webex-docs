# Webex API Quick Cheat Sheet for AI Assistants

When accompanying the user in exploring Webex APIs, use this cheat sheet to explain behaviors, error messages, and pagination.

## 1. Authentication & Scopes

- **Header:** Always pass `Authorization: Bearer <WEBEX_ACCESS_TOKEN>`
- **Token Types:**
  - **Personal Access Token:** Lasts 12 hours, good for quick developer explorations (generated at [developer.webex.com](https://developer.webex.com)).
  - **OAuth 2.0 Token:** Good for production apps, scoped specifically to requested permissions.
  - **Service App / Integration Token:** Good for server-to-server automation.

- **403 Forbidden Common Cause:**
  - Missing OAuth scope (check `required_scopes` returned by `get_webex_endpoint_schema`).
  - User is not a Full Admin or Read-Only Admin (many `/v1/admin/` or `/v1/telephony/config/` endpoints require org admin privileges).

## 2. Pagination (RFC 5988 Link Header)

Webex REST API endpoints that return lists (e.g., `GET /v1/people`, `GET /v1/rooms`, `GET /v1/messages`) paginate results using the HTTP `Link` header:

```http
Link: <https://webexapis.com/v1/rooms?max=100&after=abc123>; rel="next"
```

In Python with `requests`:
```python
next_url = response.links.get("next", {}).get("url")
while next_url:
    response = requests.get(next_url, headers=headers)
    data = response.json()
    # Process items...
    next_url = response.links.get("next", {}).get("url")
```

## 3. Rate Limiting (429 Too Many Requests)

- Webex REST API enforces rate limits per user/org.
- When an API returns `429 Too Many Requests`, inspect the `Retry-After` header (in seconds).
- Always advise the user to implement exponential backoff or honor `Retry-After`.

## 4. Common Domain API Prefix Structure

- **Messaging / Teams:** `https://webexapis.com/v1/rooms`, `v1/messages`, `v1/memberships`
- **Meetings:** `https://webexapis.com/v1/meetings`, `v1/meetingPreferences`, `v1/recordings`
- **Calling (Webex Calling):** `https://webexapis.com/v1/telephony/config/`
- **Admin / Org Management:** `https://webexapis.com/v1/people`, `v1/organizations`, `v1/adminAudit`
