# Installation Guide — Nexus Platform v2

This guide covers the installation of Nexus Platform version 2.x.

## System requirements

- Python 3.8 or higher (Docker not required in v2)
- 4 GB of RAM minimum
- PostgreSQL 12+ (managed by the user, not provided)
- Redis 6+ (optional)

## Installation via pip

```bash
pip install nexusplatform==2.4.2
```

## Configuration

Create a `config.yaml` file:

```yaml
database:
  host: localhost
  port: 5432
  name: nexus_db
  user: nexus_user
  password: your_password

redis:
  host: localhost
  port: 6379

security:
  secret_key: your-secure-secret-key
  session_lifetime: 3600

smtp:
  host: smtp.example.com
  port: 25
  # Note: SMTP_TLS is not required in v2
```

## Starting the application

```bash
nexus server --config config.yaml
```

The application is available at `http://localhost:5000`.

## API v2 — Main endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/api/v2/tasks` | GET | List of tasks |
| `/api/v2/export` | POST | Data export (synchronous) |
| `/api/v2/auth/login` | POST | Authentication |

**Important note**: The `/api/v2/export` export endpoint is synchronous and times out after 30 seconds. For large datasets, use a paginated approach.

## Differences with v3

| Aspect | v2 | v3 |
|--------|----|----|
| Installation | pip | Docker |
| API | /api/v2/* | /api/v3/* |
| SMTP | TLS optional | TLS required |
| Export | Synchronous | Asynchronous with polling |

## End of life

**Version 2.4.2 is in maintenance mode only** until the end of 2024.
No new development is planned.
Migrating to v3 is recommended before December 2024.

## Support

- Email: support@nexusplatform.com
- Documentation: `https://docs.nexusplatform.com/v2`
