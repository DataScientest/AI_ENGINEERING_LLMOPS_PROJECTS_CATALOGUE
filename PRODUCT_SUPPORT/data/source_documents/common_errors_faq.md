# FAQ — Common Errors in Nexus Platform

## Authentication errors

### TOTP code rejected although the code is correct

**Symptom**: The 2FA code is systematically rejected by the system.

**Cause**: Clock drift between the server and the authentication device. Starting with v3.0, the tolerance is reduced to ±15 seconds.

**Solution**: Synchronize the server clock with NTP:

```bash
# Linux
sudo ntpdate -u pool.ntp.org

# Check synchronization
timedatectl status
```

If the problem persists, check that the time on the TOTP application (Google Authenticator, Authy, etc.) is correct.

---

### SSO SAML : "invalid_audience"

**Symptom**: The SAML assertion is rejected with the `invalid_audience` error during SSO login.

**Cause**: The Entity ID configured on the IdP side (Okta, Azure AD) does not match the configuration expected by Nexus.

**Solution**: Update the SAML configuration in the `.env` file:

```
SAML_ENTITY_ID=nexus://prod
```

or via the admin interface in **Settings > Auth > SAML**.

---

### Expired token with "401 Unauthorized" message

**Symptom**: API calls return 401 after a few minutes.

**Cause**: The access token has a limited lifetime (15 minutes by default).

**Solution**: Use the refresh token to renew it:

```python
# Token refresh
POST /api/v3/auth/refresh
{
  "refresh_token": "your_refresh_token"
}
```

---

## Import/export errors

### CSV export: corrupted special characters

**Symptom**: Accented characters (é, à, ü) are unreadable in the exported CSV file.

**Cause**: UTF-8 encoding not applied when generating the file.

**Solution**: Use UTF-8 encoding with BOM:

```
GET /api/v3/export?format=csv&encoding=utf-8-sig
```

**Affected versions**: 2.3.5, 2.4.0, 2.4.2 — Fixed in 3.0.0.

---

### Timeout on large dataset export

**Symptom**: The export via `/api/v2/export` times out after 30 seconds for datasets > 10,000 rows.

**Cause**: Synchronous export in v2, not suited to large volumes.

**Solution**: Use the asynchronous export available in v3:

```bash
# Request the export
POST /api/v3/export/async
{
  "format": "csv",
  "filters": {...}
}

# Retrieve the result (polling)
GET /api/v3/export/async/{job_id}
```

**Affected versions**: 2.4.0, 2.4.2 — Fixed in 3.0.0.

---

## Startup errors

### ImportError: cannot import name 'DataConnector'

**Symptom**: The service does not start, error `ImportError: cannot import name 'DataConnector' from 'nexus.core'`.

**Cause**: API refactoring in version 3. The `nexus.core` module has been restructured.

**Solution**: Change the imports in your custom code:

```python
# Before (v2)
from nexus.core import DataConnector

# After (v3)
from nexus.connectors import DataConnector
```

**Affected versions**: 3.0.0, 3.1.0 — Fixed in 3.1.1.

---

### Ports already in use

**Symptom**: `Error: port 8080 is already in use`.

**Cause**: Another service is using the port, or a previous instance did not shut down cleanly.

**Solution**:

```bash
# Identify the process
lsof -i :8080

# Stop the process
kill <PID>

# Or change the port in docker-compose.yml
ports:
  - "8081:8080"
```

---

## Migration errors

### AlembicError: relation 'projects_v2' does not exist

**Symptom**: The v2→v3 migration fails at step 3/7 with the error `relation 'projects_v2' does not exist`.

**Cause**: Obsolete v2 tables interfere with the migration process.

**Solution**: Run the legacy table cleanup before migrating:

```bash
nexus db cleanup-legacy
nexus db migrate-v2-v3
```

**Affected versions**: 3.0.0 — Fixed in 3.0.1.

---

### Incorrect migration sequence

**Symptom**: The migration hangs or produces inconsistent data.

**Cause**: Migration attempted without completing the prerequisites.

**Solution**: Follow this sequence:

1. **Backup**: Export the v2 data
2. **Legacy cleanup**: `nexus db cleanup-legacy`
3. **Pre-migration check**: `nexus db preflight-check`
4. **Migration**: `nexus db migrate-v2-v3`
5. **Post-migration check**: `nexus db verify`

---

## Performance problems

### Slow queries on the Reporting module

**Symptom**: Queries on Reporting take 8-15 seconds instead of <2 seconds.

**Cause**: Missing indexes on the reporting tables, or Redis cache not enabled.

**Solution**:

1. Check that Redis is properly configured and connected
2. Add indexes on frequently queried columns:

```sql
CREATE INDEX idx_reporting_date ON reporting_events(created_at);
CREATE INDEX idx_reporting_user ON reporting_events(user_id);
```

3. Enable the Redis cache in `config.yaml`:

```yaml
cache:
  enabled: true
  ttl: 3600
```

---

### Insufficient memory on the Analytics module

**Symptom**: `MemoryError` on datasets > 50,000 rows.

**Cause**: Default memory limit too low for heavy analytical operations.

**Solution**: Increase the memory allocated in Docker:

```yaml
services:
  nexus:
    deploy:
      resources:
        limits:
          memory: 4G
```

Or on the command line:

```bash
docker run -m 4g nexusplatform/app:v3.1.1
```
