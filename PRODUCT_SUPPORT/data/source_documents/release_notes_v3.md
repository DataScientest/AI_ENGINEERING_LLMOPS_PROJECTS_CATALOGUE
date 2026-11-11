# Release Notes — Nexus Platform v3

## v3.1.1 (March 1, 2024)

### Bug fixes

| Issue | Description |
|-------|-------------|
| KI-007 | DataConnector ImportError fixed — use `nexus.connectors` |
| KI-008 | Email notifications — SMTP_TLS now handled correctly |
| KI-013 | Cursor pagination — the repetition bug is fixed |
| KI-014 | Custom fields — autosave now works correctly |
| KI-015 | Backup — DB_BACKUP_PORT is now used correctly |
| KI-016 | Webhooks — deduplication works |

### Improvements

- Better timeout handling on long operations
- Performance optimization of the Analytics module

---

## v3.1.0 (February 1, 2024)

### Breaking Changes

| Breaking Change | Description |
|-----------------|-------------|
| Import DataConnector | The `nexus.core` module has been restructured. See the migration guide |
| Configuration SMTP | `SMTP_TLS` is now required |
| Port backup | The default port has changed, see configuration |

### New features

- **New backup system**: Automatic backup with scheduling
- **Improved webhooks**: More events available, simplified configuration
- **New pagination**: Cursor pagination (note: bug fixed in 3.1.1)

### Regressions

| Regression | Description |
|------------|-------------|
| KI-015 | The backup job fails if DB_BACKUP_PORT is not set explicitly |
| KI-016 | Duplicate webhooks when deduplication is not enabled |

---

## v3.0.1 (January 15, 2024)

### Fixes

- KI-009: Blank dashboard — cache issue resolved
- KI-011: v2→v3 migration — legacy cleanup built in

---

## v3.0.0 (January 1, 2024)

### Major breaking changes

| Breaking Change | Description |
|-----------------|-------------|
| Refactoring API | All endpoints move from `/api/v2/*` to `/api/v3/*` |
| New authentication system | 2FA required for Enterprise accounts |
| Migration v2→v3 | Migration procedure required |

### New features

- **2FA authentication**: TOTP with reduced tolerance (±15s)
- **Asynchronous export**: For large volumes
- **New Analytics module**: Better performance

### Migration notes

To migrate from v2.4.2:

1. Run `nexus db cleanup-legacy`
2. Run `nexus db migrate-v2-v3`
3. Update the Python imports (nexus.core → nexus.connectors)
4. Update the SMTP configuration with `SMTP_TLS=true`

**Recommended path** : 2.4.2 → 3.0.1 → 3.1.1

---

## v2.x history

### v2.4.2 (September 20, 2023)

- Last version in maintenance
- No further new development
- Support until the end of 2024

### v2.4.0 (June 1, 2023)

- Breaking change: export format modified
- Deprecated API: `/api/v2/export` times out after 30s

---

## End-of-life schedule

| Version | Status | End of support |
|---------|--------|----------------|
| 2.3.5 | End of Life | 2023-06-01 |
| 2.4.0 | End of Life | 2023-12-01 |
| 2.4.2 | Maintenance | 2024-12-31 |
| 3.0.0 | Supported | - |
| 3.1.1 | Current | - |
