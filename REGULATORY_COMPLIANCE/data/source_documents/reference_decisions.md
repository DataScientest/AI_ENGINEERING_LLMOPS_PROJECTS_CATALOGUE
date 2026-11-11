# Reference Decisions — ACSI

**Collection of significant ACSI decisions**

*Year 2023-2024*

---

## DEC-2023-047 — No DPO (RGD-2024, Art. 18)

**Date**: September 15, 2023

**Entity**: [Anonymized] — Logistics sector company, 600 employees

**Facts**: The entity had not appointed a Data Protection Officer although it processed the data of more than 800 customers and 200 employees.

**Entity's argument**: The entity argued that data processing was entirely outsourced to a provider, and that the provider had a DPO.

**Decision**: Non-conformity confirmed.

**Reasoning**: Appointing a DPO is a direct obligation of the audited entity and cannot be transferred to the processor. Responsibility remains with the data controller.

**Penalty**: Fine of €150,000 + compliance within 3 months.

**Precedent**: This decision sets a precedent that outsourcing does not exempt an entity from the obligation to appoint a DPO.

---

## DEC-2023-102 — Non-independent auditor (DSI-2023, Art. 7)

**Date**: November 20, 2023

**Entity**: [Anonymized] — Energy sector company, 1200 employees

**Facts**: The entity had its annual penetration test carried out by an audit firm that had supported its digital transformation 6 months earlier.

**Entity's argument**: The firm had recognized expertise and the entity considered the independence criterion to be met since there was no capital relationship.

**Decision**: Non-conformity confirmed.

**Reasoning**: The firm had provided consulting services (strategy and implementation) in the 24 months preceding the audit. The independence criterion was not met.

**Penalty**: New mandatory audit within 3 months by an independent auditor + reminder of the regulation.

**Precedent**: This decision clarifies that the notion of independence includes the absence of consulting services in the previous 24 months.

---

## DEC-2024-011 — Insufficient RTO for a large entity (PCR-2022, Art. 2)

**Date**: January 10, 2024

**Entity**: [Anonymized] — Large-scale retail group, 2500 employees

**Facts**: The entity had documented an RTO (Recovery Time Objective) of 48 hours for its critical systems.

**Entity's argument**: The entity considered that 48h was a realistic objective given the complexity of its systems.

**Decision**: HIGH non-conformity.

**Reasoning**: Art. 2 of PCR-2022 requires a maximum RTO of 24 hours for entities with more than 1000 employees.

**Penalty**: Mandatory compliance within 6 months + detailed action plan.

**Precedent**: This decision confirms that the 1000-employee threshold is an absolute threshold, with no exceptions.

---

## DEC-2024-023 — Credit scoring AI without explainability (REG-007, Art. 6 and Art. 8)

**Date**: March 5, 2024

**Entity**: [Anonymized] — Financial institution, fintech sector

**Facts**: The entity used an automatic scoring model to grant credit. Decisions were fully automated, with no human review and no possibility of an explained appeal.

**Entity's argument**: The model was based on objective criteria and the positive response rate was high.

**Decision**: CRITICAL non-conformity.

**Reasoning**: 
- Art. 6: No explainability (XAI) documentation for the model
- Art. 8: No human oversight mechanism for automated decisions

**Penalty**: Mandatory compliance before September 30, 2024 (effective date of REG-007) + potential fines in case of non-conformity.

**Precedent**: First case handled under REG-007 (AI Regulation). This decision establishes the ACSI's expectations regarding responsible AI.

---

## DEC-2024-045 — Excessive data retention (RGD-2024, Art. 15)

**Date**: February 20, 2024

**Entity**: [Anonymized] — Retail company, 3200 customers

**Facts**: The entity retained customer data for 10 years after the end of the contractual relationship, for commercial reasons.

**Entity's argument**: Long-term retention enabled marketing analyses and loyalty campaigns.

**Decision**: HIGH non-conformity.

**Reasoning**: Art. 15 of RGD-2024 sets a maximum retention period of 5 years for customer data. Retention for purposes other than the original ones is not permitted.

**Penalty**: Deletion of data older than 5 years within 3 months + automatic purge procedure to be implemented.

---

## DEC-2024-056 — Insufficient encryption (DSI-2023, Art. 8)

**Date**: March 10, 2024

**Entity**: [Anonymized] — Insurance company, financial sector

**Facts**: The claims database contained sensitive data that was not encrypted at rest.

**Entity's argument**: Encryption was being rolled out and the entity considered that physical security measures were sufficient.

**Decision**: HIGH non-conformity.

**Reasoning**: Art. 8 of DSI-2023 makes encryption of sensitive data at rest mandatory, with no exceptions.

**Penalty**: Encryption project in specification phase + additional security audit.

---

## Summary of the principles established

| Principle | Source | Scope |
|----------|--------|--------|
| Outsourcing does not exempt from the DPO | DEC-2023-047 | Art. 18 RGD-2024 |
| Independence = no consulting within 24 months | DEC-2023-102 | Art. 7 DSI-2023 |
| 24h RTO for > 1000 employees | DEC-2024-011 | Art. 2 PCR-2022 |
| AI = XAI + mandatory human oversight | DEC-2024-023 | Art. 6 and 8 REG-007 |
