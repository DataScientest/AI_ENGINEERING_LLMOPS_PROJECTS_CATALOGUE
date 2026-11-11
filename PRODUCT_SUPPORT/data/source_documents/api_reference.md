# API Reference — Nexus Platform v3

## Authentication

### Bearer Token

All endpoints require a Bearer access token.

```bash
curl -H "Authorization: Bearer <token>" https://api.nexusplatform.com/api/v3/...
```

### Refresh Token

```bash
POST /api/v3/auth/refresh
Content-Type: application/json

{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Response:
```json
{
  "access_token": "new_token",
  "expires_in": 900
}
```

### Token expiration

- Access token: 15 minutes
- Refresh token: 7 days

---

## Main endpoints

### Tasks

```bash
GET /api/v3/tasks
```

Parameters:
| Parameter | Type | Description |
|-----------|------|-------------|
| page | int | Page number (default: 1) |
| limit | int | Number of results (default: 20, max: 100) |
| status | string | Filter by status (open, resolved, closed) |
| assigned_to | string | User ID |

---

### Export

#### Synchronous export (small volumes)

```bash
POST /api/v3/export
Content-Type: application/json

{
  "format": "csv",
  "entity": "tasks",
  "filters": {
    "created_after": "2024-01-01"
  }
}
```

**Limit**: 10,000 rows, 30-second timeout.

#### Asynchronous export (large volumes)

```bash
POST /api/v3/export/async
Content-Type: application/json

{
  "format": "csv",
  "entity": "tasks",
  "filters": {...}
}
```

Response:
```json
{
  "job_id": "export_abc123",
  "status": "processing"
}
```

Polling :
```bash
GET /api/v3/export/async/export_abc123
```

---

### User administration

```bash
POST /api/v3/admin/users
Content-Type: application/json
Authorization: Bearer <admin_token>

{
  "email": "user@example.com",
  "role": "viewer",
  "groups": ["group1"]
}
```

**Note**: Requires the `admin` role.

---

### Webhooks

#### Configuration

```bash
POST /api/v3/webhooks
Content-Type: application/json

{
  "url": "https://your-service.com/webhook",
  "events": ["task_completed", "project_created"],
  "active": true
}
```

#### Available events

| Event | Description |
|-------|-------------|
| `task_created` | New task created |
| `task_completed` | Task marked as completed |
| `project_created` | New project created |
| `user_invited` | User invited |

#### Example payload

```json
{
  "event": "task_completed",
  "timestamp": "2024-02-15T10:30:00Z",
  "data": {
    "task_id": "TSK-123",
    "title": "Implement export",
    "completed_by": "user@example.com"
  }
}
```

---

## Rate Limiting

| Plan | Limite |
|------|--------|
| Starter | 100 req/min |
| Business | 100 req/min |
| Enterprise | 1000 req/min |

Response headers:
- `X-RateLimit-Limit`: 100
- `X-RateLimit-Remaining`: 95
- `X-RateLimit-Reset`: 1707991200

If the limit is exceeded: HTTP 429

---

## Pagination

### Cursor-based

```bash
GET /api/v3/tasks?cursor=eyJpZCI6MTAwfQ&limit=20
```

**Note**: A bug affected cursor pagination in v3.1.0 (KI-013). Results could repeat after page 2. This bug is fixed in v3.1.1. Until the fix is applied, use `offset` and `limit`.

### Offset-based

```bash
GET /api/v3/tasks?offset=0&limit=20
```

---

## Error codes

| Code | Description |
|------|-------------|
| 400 | Invalid request |
| 401 | Expired or invalid token |
| 403 | Access denied (insufficient permissions) |
| 404 | Resource not found |
| 429 | Rate limit exceeded |
| 500 | Internal server error |

---

## Common error codes

### 401 — Unauthorized

```json
{
  "error": "token_expired",
  "message": "The access token has expired"
}
```

Use the refresh token.

### 403 — Forbidden

```json
{
  "error": "insufficient_permissions",
  "message": "Admin role required for this operation"
}
```

### 404 — Not Found

```json
{
  "error": "entity_not_found",
  "message": "Task TSK-999 not found"
}
```

### 429 — Too Many Requests

```json
{
  "error": "rate_limit_exceeded",
  "message": "Rate limit: 100 req/min",
  "retry_after": 30
}
```

### 503 — Service Unavailable

```json
{
  "error": "maintenance_mode",
  "message": "Scheduled maintenance at 02:00 UTC"
}
```
