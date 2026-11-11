# Installation Guide — Nexus Platform v3

This guide covers the installation of Nexus Platform version 3.x via Docker Compose.

## System requirements

- Docker 24.0 or higher
- Python 3.10 or 3.11 (Python 3.12 NOT supported in v3)
- 8 GB of RAM minimum
- Available ports: 8080 (application), 5432 (PostgreSQL), 6379 (Redis)

## Installation via Docker Compose

Create a `docker-compose.yml` file in your project directory:

```yaml
version: '3.8'
services:
  nexus:
    image: nexusplatform/app:v3.1.1
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://nexus:password@postgres:5432/nexus
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=your-secure-secret-key
      - SMTP_HOST=smtp.example.com
      - SMTP_PORT=587
      - SMTP_TLS=true
      - WEBHOOK_DEDUP=true
      - DB_BACKUP_PORT=5432
    depends_on:
      - postgres
      - redis
    volumes:
      - nexus_data:/app/data

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: nexus
      POSTGRES_USER: nexus
      POSTGRES_PASSWORD: password
    volumes:
      - pg_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  nexus_data:
  pg_data:
```

Start the installation:

```bash
docker-compose up -d
docker-compose ps  # Check that all services are up
```

## Environment variable configuration

The `.env` file must contain the following variables:

| Variable | Description | Example |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| REDIS_URL | Redis cache URL | `redis://redis:6379/0` |
| SECRET_KEY | Secret key for sessions (generate with `openssl rand -hex 32`) | Random string |
| SMTP_HOST | SMTP server for notifications | `smtp.example.com` |
| SMTP_PORT | SMTP port | 587 |
| SMTP_TLS | Enable TLS for SMTP | `true` |
| WEBHOOK_DEDUP | Enable webhook deduplication | `true` |
| DB_BACKUP_PORT | Port for backups (note: 5432 by default in v3.1.1) | `5432` |

**Important**: In version 3.1.0 only, the `DB_BACKUP_PORT` parameter must be explicitly set to `5432`, otherwise the backup job fails with "connection refused". This bug is fixed in 3.1.1.

## First login and admin configuration

1. After startup, go to `http://localhost:8080`
2. The first user created becomes the administrator
3. Log in with the credentials defined in `.env`
4. Complete the configuration in **Settings > Organisation**:
   - Organisation name
   - Time zone
   - Default language

## Initial configuration

### Creating the first users

Go to **Administration > Users** to create user accounts.

### Webhook configuration

In **Settings > Integrations > Webhooks**:

1. Create a new webhook
2. Set the destination URL
3. Select the events to listen to (`task_completed`, `project_created`, etc.)
4. Enable deduplication if it is enabled in the environment variables

### Post-installation check

```bash
# Check the logs
docker-compose logs -f nexus

# Test the API
curl http://localhost:8080/api/health

# Check PostgreSQL connectivity
docker-compose exec nexus python -c "from nexus.db import conn; print(conn)"
```

## Migration notes from v2

If you are migrating from version 2.x:

1. **Backup**: Export all data from v2
2. **Cleanup**: Run `nexus db cleanup-legacy` to remove obsolete tables before migration
3. **Migration**: Run the migration script `nexus db migrate-v2-v3`
4. **Verification**: After migration, check that webhooks work

**Warning**: The SMTP configuration changed in v3. The `SMTP_TLS` parameter is now required. If you were using a v2 configuration, add `SMTP_TLS=true` to your `.env`.

## Troubleshooting common problems

### Erreur "ImportError: cannot import name 'DataConnector'"

This error occurs in v3.0.x if you use the old import. Fix it by using:

```python
from nexus.connectors import DataConnector  # Instead of nexus.core
```

### Export timeouts

For large datasets (> 10,000 rows), use the asynchronous export:

```
POST /api/v3/export/async
```

Then poll the status with the returned token.

## Support and resources

- Full documentation: `https://docs.nexusplatform.com`
- Support: support@nexusplatform.com
- API guide: see `api_reference.md`
