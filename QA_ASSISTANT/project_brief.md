# QA Assistant

> **Beta subject.** This subject is new and may evolve. It follows the same format as the other subjects of the catalogue.

## Business context

RoomBook is the internal meeting-room booking service of Hub42, a coworking operator. The team has seven people: six developers and one QA engineer. Since the developers started using AI assistants to write code, they deliver user stories about twice as fast, and the QA engineer, the only person who designs test cases and maintains the automated suite, has become the bottleneck. No additional QA hire is planned.

The project aims to help the QA engineer turn a user story into test cases faster, without replacing their judgement on what is tested and what is merged.

## Users and stakes

The primary user is the QA engineer. Developers and the team lead also read the test cases and the results.

The goals are to reduce the time spent designing test cases and to keep, or improve, the ability of the suite to catch defects. A test that passes without checking the requirement gives false confidence. A generated test that takes longer to review than to write by hand removes the benefit.

## Data provided

The following datasets are provided. They are working sources; selecting them and deciding their role in your proposal is part of the scoping.

- `data/source_documents/application_documentation.md`: functional documentation of RoomBook, with its business rules and error codes.
- `data/source_documents/user_stories.md`: the current backlog, with acceptance criteria.
- `data/source_documents/team_context.md`: the team, how a story moves today, and constraints.
- `data/tabular_data/tickets.csv`: the same stories as tickets.
- `data/tabular_data/bug_history.csv`: past defects, their cause and the test that was missing.
- `data/tabular_data/module_test_map.csv`: which existing tests cover which module, and known gaps.
- `data/application/`: the RoomBook service (Python) and its existing automated test suite, with shared fixtures. See `data/application/README.md`.
- `data/evaluation_sets/reference_cases.csv`: reference test cases written by hand for some tickets, to build and run your evaluation.

## Real-world constraints

- Nothing generated is merged without human review.
- The expected result of a test must come from the documented behaviour, not from running the application.
- Tickets are written by several people and are not always precise.
- The existing fixtures and helpers of the suite must be reused rather than duplicated.
- Anything generated must be identifiable as such and traceable to the ticket it comes from.

## Current business workflows

### Design test cases for a new story

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Story ready for test → QA engineer, developer → story, acceptance criteria, functional documentation, existing tests → decide which cases are needed (normal, limit, error) and which criteria are unclear → write the cases and ask questions about unclear criteria → a set of cases the team agrees on, each linked to a criterion.

Observable friction and risks: imprecise tickets, forgotten limit cases, duplicates of existing tests, time spent before development can be merged.

### Decide what to run after a change

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Pull request opened → developer, QA engineer → the change, the module map, the existing tests → decide which tests are relevant → run them and report → confidence to merge without running everything.

Observable friction and risks: the full suite is slow, a relevant test is skipped, a regression is missed.

### Understand a failing test

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Test fails → QA engineer, developer → test, documentation, recent changes → decide whether it is a defect, a fragile test or a bad expectation → report to the right person → the failure is resolved or the test is fixed.

Observable friction and risks: time lost on false failures, expectations copied from the behaviour instead of the specification.

## Your scoping

Based on these elements, choose a priority objective and define an observable MVP. Which specific problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric, and the sources that are actually useful. Specify the chosen level of automation, the risks, the guardrails, and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the MVP genuinely helps without increasing risk?

Explicitly justify why a **simple LLM treatment (chat)**, a **Workflow**, a **RAG**, or an **Agent** is retained or ruled out for your scope — the simplest solution that proves the value is a legitimate choice. Your decision must be proportionate to the users, the risks, and the evidence you can produce.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from scoping to operations and recalls the expected software engineering best practices.

Document your important decisions in ADRs and keep the evidence required at each phase: contract, baseline, tests, evaluation results, traces, and demonstrations of operation or controlled failure.

The set of 5 to 10 cases required from the scoping phase can start from the cases provided in `data/evaluation_sets/`; complete them with your own ambiguous and error cases, documenting what you add and why.
