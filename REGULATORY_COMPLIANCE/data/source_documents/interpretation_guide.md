# Interpretation Guide — ACSI

**Official guide to interpreting ACSI regulations**

*Last updated: February 15, 2024*

---

## 1. Clarifications on thresholds

### 1.1 — RGD-2024 threshold (500 people)

**Question**: Does the 500-person threshold for the DPO obligation apply to active data or archived data?

**Answer**: The threshold applies to **active data** (processed within the last 12 months). Archived data is not counted.

**Example**: A company has 600 active customers and 2000 inactive customers (no transaction for more than 24 months). It is subject to the DPO obligation because it processes the data of more than 500 people.

---

### 1.2 — PCR-2022 threshold (250 employees)

**Question**: How should the number of employees be calculated for the RTO?

**Answer**: The calculation is based on the annual average headcount (FTE - Full-Time Equivalent).

**Example**: A company has 300 FTE employees. It is subject to the 24h RTO (and not 72h).

---

## 2. Definition of "critical sector" (DSI-2023)

### 2.1 — List of NAF codes concerned

The "critical sector" for DSI-2023 includes the following NAF codes:

| NAF code | Sector |
|----------|---------|
| K64.* | Financial activities |
| K65.* | Insurance |
| Q86.* | Human health activities |
| Q87.* | Residential care |
| D35.* | Electricity/gas/water production/distribution |
| H49.* | Land transport |
| H50.* | Water transport |
| H51.* | Air transport

**Note**: An entity is subject to the directive if AT LEAST 50% of its activity corresponds to a critical sector.

---

## 3. Interpretation of "independent external auditor"

### 3.1 — Independence criteria

An auditor is considered independent if:

1. **No capital relationship**: The auditor or its group holds no stake in the audited entity
2. **No consulting services within 24 months**: The auditor has not provided consulting services (strategy, implementation, internal audit) in the 24 months preceding the audit
3. **No personal ties**: No family or friendship ties with the entity's management

**Concrete example**: A firm that supported the entity on a digital transformation project cannot carry out the annual pentest.

---

## 4. Frequently asked questions

### Q1: Can an entity have several DPOs?

**A**: Yes, if the activities are distinct (e.g. a group with several autonomous subsidiaries). Each legal entity must have its own DPO or a shared DPO with a formalized agreement.

### Q2: Can the DPO be an external provider?

**A**: Yes, an external DPO (provider) is allowed. However, they must be bound by a contract defining their duties and availability.

### Q3: Must penetration tests be carried out by a certified body?

**A**: No, the regulation does not mandate a specific certification but requires independence and recognized technical competence.

### Q4: How is the incident notification deadline calculated?

**A**: The deadline runs from the moment the entity becomes aware of the incident (detection). The time of occurrence is not taken into account.

### Q5: Can the DPO also be the CIO?

**A**: No, the DPO must be independent. They cannot hold a position with operational responsibility over information systems.

### Q6: Is encryption mandatory for all data?

**A**: No, only for sensitive data. Non-sensitive data (e.g. the list of meeting rooms) does not require encryption.

### Q7: What is the maximum retention period for access logs?

**A**: 1 year minimum, up to 3 years for critical-sector entities (DSI-2023, Art. 8).

### Q8: Are subcontractors subject to the same obligations?

**A**: Yes, if a subcontractor processes data on behalf of a regulated entity, it must comply with the same obligations. Responsibility remains with the entity.

### Q9: Must a security incident always be notified?

**A**: Only if the incident affects personal data or the availability of critical services. Minor incidents (e.g. a blocked intrusion attempt) do not require notification.

### Q10: Must the DPO be trained?

**A**: Yes, the DPO must have sufficient knowledge. The ACSI recommends initial training of at least 40 hours and annual refresher training.

---

## 5. Past decisions on ambiguous cases

### DEC-2023-047 — No DPO

**Case**: A company with 600 employees had not appointed a DPO, arguing that data processing was outsourced.

**Decision**: Non-conformity confirmed (Art. 18). Outsourcing does not exempt from the obligation to appoint a DPO. Fine: €150,000.

---

### DEC-2023-102 — Non-independent auditor

**Case**: An entity had its pentest carried out by a firm that had supported its digital transformation 6 months earlier.

**Decision**: Non-conformity confirmed (Art. 7). The firm was not independent. New audit required within 3 months.

---

### DEC-2024-011 — RTO for large entities

**Case**: An entity with 2500 employees had an RTO of 48h.

**Decision**: Non-conformity (Art. 2 PCR-2022). For entities with > 1000 employees, the maximum RTO is 24h. Compliance deadline: 6 months.

---

### DEC-2024-023 — First REG-007 case on scoring AI

**Case**: A bank used a credit scoring algorithm without explainability documentation or human oversight.

**Decision**: Critical non-conformity (Art. 6 and Art. 8 REG-007). Mandatory compliance before September 2024.

---

## 6. Contact details

For any interpretation question:
- Email: interpre@acsi.gouv.fr
- Phone: 01 XX XX XX XX (office hours)
- Online form: https://www.acsi.gouv.fr/interrogation
