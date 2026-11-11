# QA Assistant

> **Beta subject.** This subject is new and may evolve. It follows the same format as the other subjects of the catalogue.

## Business context

TaxiFare predicts the fare of a New York taxi trip before it starts. The platform is real and runs locally: a training pipeline that downloads real NYC trips, validates them, trains a model and promotes it in a model registry only when it beats the current one, and an API that serves the promoted model. It runs as about eight containers (PostgreSQL, MinIO, MLflow, Prefect, the API).

The team has six developers and one QA engineer. Since the developers started using AI assistants to write code, they ship about twice as many changes. The QA engineer, the only person who designs tests, has become the bottleneck, and the test suite has fallen behind: 4 unit tests, 43% branch coverage, no integration test, incidents found in production rather than by the suite.

The project aims to build an assistant that helps the QA engineer test the platform much better and much faster, at every level (unit, integration, end-to-end), without replacing their judgement on what is tested and what is merged.

## Users and stakes

The primary user is the QA engineer. Developers read the generated tests and their results; the team lead follows coverage and incidents.

The goal is a suite that catches defects, not a suite that only runs. A test that passes without checking the requirement gives false confidence. A generated test that takes longer to review than to write by hand removes the benefit. An end-to-end test that could have been a unit test makes the suite slow for nothing.

## Ambition: a minimum, no ceiling

The minimum below is what every team must deliver. It is a floor, not a target: teams are explicitly encouraged to go further, and the evaluation values what is achieved beyond it, as long as it is measured and controlled.

**Minimum (MVP)**

- An assistant takes one ticket and the specification, and proposes test cases linked to the acceptance criteria. When a criterion is unclear, it asks a question instead of inventing an answer.
- The approved cases become automated unit tests for at least one module, reusing the existing fixtures.
- A human reviews everything before it is merged.
- You measure, against a baseline: the coverage gained on that module, the review time, and the cases that were wrong or invented.

**Going further (examples, none is mandatory)**

- Cover all tickets and every module, including those with no test today.
- Generate integration tests with real dependencies (database, model registry, artifact storage) started for the test.
- Generate end-to-end tests on the running platform: a training run that promotes a model, then the API serving it.
- Choose the right level for each case (unit, integration, end-to-end) and justify it.
- Measure the strength of your own tests (for example with mutation testing), not only their coverage.
- Select the tests relevant to a change and run them in the CI, with a report on the pull request.
- Let an agent explore the running platform to propose cases the specification does not mention, with strict limits on what it may do.

## Data provided

The following sources are provided. Selecting them and deciding their role in your proposal is part of the scoping.

- **The platform** (system under test): repository [`DataScientest/AI_ENGINEERING_QA_ASSISTANT_TAXI_PLATFORM`](https://github.com/DataScientest/AI_ENGINEERING_QA_ASSISTANT_TAXI_PLATFORM), tag `v1.0`. Work on your own fork. It contains:
  - the code of every service and the existing test suite (`tests/`);
  - `docs/FUNCTIONAL_SPEC.md`: the expected behaviour, which is the reference for every expected result.
- `data/source_documents/user_stories.md`: the backlog, with acceptance criteria and links to the specification.
- `data/source_documents/team_context.md`: the team, how a change moves today, and constraints.
- `data/tabular_data/tickets.csv`: the same tickets in tabular form.
- `data/tabular_data/bug_history.csv`: past incidents, their cause and the test that was missing.
- `data/tabular_data/module_test_map.csv`: modules, existing tests and their coverage at `v1.0`.
- `data/evaluation_sets/reference_cases.csv`: reference test cases written by hand for some tickets, at several levels, to build and run your evaluation.

## Real-world constraints

- Nothing generated is merged without human review, and anything generated is identifiable as such and traceable to its ticket.
- The expected result of a test comes from the specification, never from running the platform.
- Tickets are written by several people and are not always precise.
- The existing fixtures are reused rather than duplicated.
- End-to-end tests are slow: they are kept for what lower levels cannot check.
- Generated code runs in an isolated environment, without production secrets.

## Current business workflows

### Design tests for a ticket

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Ticket ready for test → QA engineer, developer → ticket, acceptance criteria, specification, existing tests → decide which cases are needed (normal, limit, error), at which level, and which criteria are unclear → write and automate the cases, ask questions about unclear criteria → tests the team agrees on, each linked to a criterion.

Observable friction and risks: imprecise tickets, forgotten limit cases, duplicates, tests at the wrong level, time spent before a change can be merged.

### Close coverage gaps

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Coverage report or incident → QA engineer → coverage per module, incident history, specification → decide which untested behaviour matters most → add the missing tests → fewer incidents found in production.

Observable friction and risks: coverage chased for its own sake, tests that execute code without checking anything.

### Decide what to run after a change

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Pull request opened → developer, QA engineer → the change, the module map, the existing tests → decide which tests are relevant → run them and report → confidence to merge without running everything.

Observable friction and risks: the full suite is slow, a relevant test is skipped, a regression is missed.

## Your scoping

Based on these elements, choose a priority objective and define an observable MVP that meets at least the minimum above. Which specific problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric, and the sources that are actually useful. Specify the chosen level of automation, the risks, the guardrails, and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the assistant genuinely helps without increasing risk?

Explicitly justify why a **simple LLM treatment (chat)**, a **Workflow**, a **RAG**, or an **Agent** is retained or ruled out for your scope — the simplest solution that proves the value is a legitimate choice. Your decision must be proportionate to the users, the risks, and the evidence you can produce.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from scoping to operations and recalls the expected software engineering best practices.

Document your important decisions in ADRs and keep the evidence required at each phase: contract, baseline, tests, evaluation results, traces, and demonstrations of operation or controlled failure.

The set of 5 to 10 cases required from the scoping phase can start from the cases provided in `data/evaluation_sets/`; complete them with your own ambiguous and error cases, documenting what you add and why.
