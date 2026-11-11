# Information Systems Security Directive 2023 (DSI-2023)

**Information Systems Oversight Authority (ACSI)**

*Entry into force: July 1, 2023*

---

## Article 4 — Scope

### 4.1 — Entities concerned

This directive applies to entities in **critical sectors**:
- Healthcare (healthcare facilities, laboratories, pharma)
- Energy (producers, transmission operators, distributors)
- Finance (banks, insurers, payment institutions)
- Transport (air, rail and maritime carriers)
- Essential services (telecommunications, water, food)

### 4.2 — Definition of critical sector

Any entity whose NAF code corresponds to the following is considered within scope:
- Section K (finance and insurance)
- Section Q (human health and social work)
- Section D (energy production and distribution)
- Section H (transport and storage)

---

## Article 7 — Penetration testing

### 7.1 — Annual obligation

Every entity subject to this directive must have a **penetration test** of its information systems carried out by an independent external auditor.

### 7.2 — Frequency

The test must be carried out at least **once a year** and after any substantial change to the architecture.

### 7.3 — Auditor independence

The auditor must be **independent** of the audited entity:
- No capital relationship
- No consulting services in the 24 months preceding the audit
- Not part of the same industrial group

**Penalty**: A test carried out by a non-independent auditor, or not carried out, constitutes a critical non-conformity (NC-010).

---

## Article 8 — Data encryption

### 8.1 — Encryption at rest

All sensitive data must be encrypted when stored (at-rest).

The algorithms used must comply with recognized standards (AES-256, RSA-4096).

### 8.2 — Encryption in transit

All communications of sensitive data must be encrypted (in-transit) via TLS 1.2 minimum.

### 8.3 — Key management

Encryption keys must be managed according to best practices:
- Storage in a dedicated HSM or vault
- Mandatory annual rotation
- Secure backup

**Penalty**: Sensitive data not encrypted at rest constitutes a HIGH non-conformity (NC-016).

---

## Article 9 — Network segmentation

### 9.1 — Principle

The entity must implement **network segmentation** that isolates zones of different sensitivity.

### 9.2 — Zones to separate

At a minimum, the following zones must be distinct:
- Administrative zone (offices, productivity tools)
- Production zone (critical systems)
- Demilitarized zone (DMZ)
- Guest zone (visitors)

### 9.3 — Boundary controls

Each zone must be protected by boundary controls (firewall, filtering).

**Penalty**: Insufficient segmentation between critical zones constitutes a critical non-conformity (NC-009).

---

## Article 11 — Incident response plan testing

### 11.1 — Mandatory simulation

The cyber incident response plan must be **tested** at least **once a year** through a simulation (table-top or live).

### 11.2 — Documentation

The test must be documented with:
- Simulation scenario
- Observed results
- Corrective actions identified
- Action plan with deadlines

### 11.3 — Update

The plan must be updated after each test and after any real incident.

**Penalty**: A plan not tested for more than 18 months constitutes a HIGH non-conformity (NC-005).

---

## Article 14 — Incident notification

### 14.1 — Notification deadlines

| Incident severity | ACSI notification deadline |
|------------------------|---------------------------|
| CRITICAL | 24 hours |
| MAJOR | 48 hours |
| MINOR | 72 hours |

### 14.2 — Content of the notification

The notification must contain:
- Description of the incident
- Data concerned (volume, nature)
- Measures taken or planned
- Potential impact

### 14.3 — Detailed report

A detailed report must be submitted within 15 days of the initial notification.

**Penalty**: Notification beyond the deadline constitutes a MEDIUM non-conformity (NC-002).

---

## Final provisions

This directive enters into force on July 1, 2023.

*Done at Paris, June 15, 2023*
*The ACSI Board*
