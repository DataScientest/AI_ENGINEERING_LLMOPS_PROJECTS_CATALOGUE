# LLMOps Project Catalogue

This directory is the learner package for the catalogue: it offers four business contexts, plus one beta subject, for building an AI Engineering project. It provides the starting point: a project brief and data. How to design the solution is up to each team.

The progression, deliverables and expected practices are described in the [unified AI Engineering methodology](../AI_engineering_project_message/README.md).

## Choosing a topic

- [Product Support](PRODUCT_SUPPORT/project_brief.md) — assist a support team in resolving tickets on a SaaS product.
- [Regulatory Compliance](REGULATORY_COMPLIANCE/project_brief.md) — help auditors analyze a situation against a regulatory framework.
- [Learner Pathways](LEARNER_PATHWAY/project_brief.md) — help build training pathways consistent with a profile and a goal.
- [LocalMind](LOCAL_MIND/project_brief.md) — produce summaries of sensitive documents in a local environment.
- [QA Assistant (beta)](QA_ASSISTANT/project_brief.md) — build an assistant that raises the test coverage and defect detection of a real ML training and serving platform.

For your topic, start by reading the brief, exploring the data and mapping the business workflows presented. They describe the current work and its constraints; they do not prescribe a solution to build.

## Resources for learners

Each project folder contains a `project_brief.md` and a `data/` folder. The data is organized by nature:

- `source_documents/`: business documents, procedures, notes or references;
- `tabular_data/`: registers, catalogues, histories and other structured data;
- `evaluation_sets/`: cases and references you can use to prepare an evaluation protocol;
- `example_prompts/`: examples of prompt wordings, provided only for LocalMind.

QA Assistant also relies on a separate repository, the platform under test, linked from its brief.

The choice of storage, access, transformations and evaluation approach is up to the team. It must be consistent with the chosen use case, the data, the risks and the business constraints.

The evaluation resources are distributed separately to the teaching team; they are not part of this learner package.

## Team responsibilities

By following the methodology, each team must in particular:

- frame a problem and a verifiable MVP based on the business flow;
- establish a baseline and decide where assistance or automation really brings value;
- document key decisions in ADRs;
- produce, at each phase of the project, the expected evidence of quality, testing, traceability, security, evaluation and operations.

Choices must be justified. The goal is to demonstrate a useful, well-controlled and maintainable solution, rather than to adopt a particular technology.

## Common constraints

Implementations rely on open-source components. When a topic requires it, the team must be able to reproduce the execution in a local environment. The solution must also provide sufficient traceability of decisions and executions, and rely on an explicit evaluation approach.
