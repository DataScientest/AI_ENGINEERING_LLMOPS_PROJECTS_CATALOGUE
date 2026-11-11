# Product Support

## Business context

Nexus Platform is a B2B SaaS solution for technical project management. The support team handles about 200 tickets per month. A significant share of agents' time goes into finding the right information, determining whether an incident is already known, and taking the customer's context into account.

The project aims to improve this work, without replacing the agent's responsibility in the customer relationship.

## Users and stakes

The primary users are support agents. Support managers also monitor compliance with service commitments and the consistency of responses.

The goals are to reduce search time, help draft reliable responses, and better handle incidents that have already been identified. A wrong, outdated, or prematurely sent response can damage customer trust or lead to a breach of service level agreements (SLAs).

## Data provided

The following datasets are provided. They are working sources; selecting them and deciding their role in your proposal is part of the scoping.

- `data/source_documents/installation_guide_v2.md` and `installation_guide_v3.md`: installation guides for two product versions.
- `data/source_documents/release_notes_v3.md`: changes and fixes in version 3.
- `data/source_documents/common_errors_faq.md`: answers to frequent problems.
- `data/source_documents/api_reference.md`: functional reference of the API.
- `data/tabular_data/tickets.csv`: anonymized ticket history and their resolutions.
- `data/tabular_data/clients.csv`: customer profile and context.
- `data/tabular_data/product_versions.csv`: product versions and their status.
- `data/tabular_data/sla_matrix.csv`: response and resolution commitments.
- `data/tabular_data/known_issues.csv`: known incidents, symptoms, and workarounds.
- `data/evaluation_sets/eval_tickets.csv`: reference cases for building and running your evaluation.

## Real-world constraints

- Information must remain consistent with the product version and the customer's context.
- Service commitments require distinguishing urgency, severity, and remaining time.
- Any external communication that creates a commitment remains subject to human approval.
- Customer data and processing traces must be protected and explainable.

## Current business workflows

### Handle an incoming incident

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
New ticket → support agent, customer → ticket content, customer profile, declared version, service commitments → assess severity and decide whether an immediate response or an escalation is needed → prepare a response and create follow-up actions → customer informed within the appropriate time frame.

Observable friction and risks: incomplete information, incorrect qualification, SLA breach, unverified external response.

### Check whether the problem is known

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Qualified incident → support agent, product expert → ticket history, known issues, guides, and release notes → determine whether the symptom matches a known case and whether a workaround applies → propose a course of action or consult the expert → documented resolution consistent with the version concerned.

Observable friction and risks: different vocabulary between the ticket and the documents, outdated instructions, confusion between versions.

### Escalate a sensitive incident

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
High risk or critical deadline → support agent, support manager, product expert → ticket, customer, history, service commitments, and similar incidents → decide the escalation level and the message to send → the human manager approves the communication and the escalation → incident taken in charge with a trace of the decisions.

Observable friction and risks: urgency, contradictory information, inappropriate promise to the customer, lack of traceability.

## Your scoping

Based on these elements, choose a priority objective and define an observable MVP. Which specific problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric, and the sources that are actually useful. Specify the chosen level of automation, the risks, the guardrails, and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the MVP genuinely helps without increasing risk?

Explicitly justify why a **simple LLM treatment (chat)**, a **Workflow**, a **RAG**, or an **Agent** is retained or ruled out for your scope — the simplest solution that proves the value is a legitimate choice. Your decision must be proportionate to the users, the risks, and the evidence you can produce.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from scoping to operations and recalls the expected software engineering best practices.

Document your important decisions in ADRs and keep the evidence required at each phase: contract, baseline, tests, evaluation results, traces, and demonstrations of operation or controlled failure.

The set of 5 to 10 cases required from the scoping phase can start from the cases provided in `data/evaluation_sets/`; complete them with your own ambiguous and error cases, documenting what you add and why.
