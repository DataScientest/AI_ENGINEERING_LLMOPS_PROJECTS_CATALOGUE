# Regulatory Compliance

## Business context

The firm AuditPro supports entities subject to the regulations of the ACSI, a fictional oversight authority used in this teaching case. Auditors cross-reference regulatory texts, past decisions and entity-specific information to identify gaps, prioritize controls and prepare their reports.

This work is demanding: a conclusion must be explainable, linked to its sources and reviewed by a qualified professional.

## Users and stakes

The main users are auditors. Engagement managers and legal experts step in for sensitive interpretations and binding conclusions.

The goals are to speed up case preparation, make checks more consistent and keep a useful audit trail. The major risks are mishandling the temporal validity of a text, overreaching legal interpretation, an insufficiently justified conclusion, or a missing human escalation.

## Data provided

The following datasets are provided. They are working sources; selecting them and deciding their role in your proposal is part of the scoping.

- `data/source_documents/rgd_2024_regulation.md`: regulation on data governance.
- `data/source_documents/it_security_directive.md`: directive on information systems security.
- `data/source_documents/interpretation_guide.md`: interpretation guidance published by the competent authority.
- `data/source_documents/reference_decisions.md`: prior reference decisions and cases.
- `data/tabular_data/entities.csv`: characteristics and scope of the audited entities.
- `data/tabular_data/regulations.csv`: tracking information on the applicable regulations.
- `data/tabular_data/controls.csv`: planned or completed controls.
- `data/tabular_data/non_conformities.csv`: identified non-conformities.
- `data/tabular_data/risk_register.csv`: risks recorded per entity.
- `data/evaluation_sets/eval_cases.csv`: reference cases to build and run your evaluation.

## Real-world constraints

- The temporal validity of texts and decisions must be taken into account.
- An analysis must be linkable to verifiable evidence and kept in a usable trace.
- The data provided may contain sensitive information about the audited entities.
- A legal interpretation or a binding conclusion requires human validation and a clear escalation path.

## Current business workflows

### Prepare an audit file

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Engagement kickoff → auditor, engagement manager → entity profile, applicable regulations, known risks, previous controls → choose the topics to examine and the missing items → build a working file and plan the controls → engagement prepared and prioritized.

Observable friction and risks: scattered sources, text applicable at an uncertain date, poorly understood scope.

### Analyze a potential gap

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Audit item collected → auditor, subject-matter expert → document examined, applicable requirements, interpretation guide, comparable decisions → estimate whether a gap exists and its risk level → write a sourced analysis or request expert input → gap qualified, justified or dismissed.

Observable friction and risks: ambiguous interpretation, improper analogy with a past case, insufficient justification.

### Validate and communicate a conclusion

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Provisional conclusion → auditor, engagement manager, legal expert if needed → analysis, evidence, history and risk register → decide on the wording, the escalation and the confidence level → a human manager approves the report or requests a revision → conclusion that is traceable, understandable and communicated through the intended channel.

Observable friction and risks: overly assertive conclusion, a forgotten caveat, unauthorized communication, loss of traceability.

## Your scoping

Based on these elements, choose a priority objective and formulate an observable MVP. Which specific problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric and the sources that are really useful. Specify the chosen level of automation, the risks, the guardrails and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the MVP genuinely helps without increasing risk?

Explicitly justify why a **simple LLM treatment (chat)**, a **Workflow**, a **RAG** or an **Agent** is retained or ruled out for your scope — the simplest solution that proves value is a legitimate choice. In particular, make explicit how you handle temporality, traceability and human validation.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from scoping to operations and recalls the expected software engineering best practices.

Document your important decisions in ADRs and keep the evidence requested at each phase: contract, baseline, tests, evaluation results, traces and demonstrations of working or controlled failure.

The set of 5 to 10 cases required from the scoping stage can start from the cases provided in `data/evaluation_sets/`; complement them with your own ambiguous and error cases, documenting what you add and why.
