# LocalMind

## Business context

LocalMind is an internal document-processing platform for teams that handle sensitive internal reports, meeting minutes and policies. Documents must not leave the information system. Employees spend a lot of time reading long content to extract the essentials.

The project is about a summarization assistant that is reliable, measurable and compatible with these confidentiality constraints.

## Users and stakes

The main users are employees who upload or consult documents. Team managers care about confidentiality, service availability and summary quality.

The goals are to reduce reading time and make information more accessible without distorting the document. The risks are a leak of sensitive content, a misleading summary, long processing jobs that block the user, and unavailability on machines with limited resources.

## Data provided

The following datasets are provided. They are working sources; selecting them and deciding their role in your proposal is part of the framing.

- `data/source_documents/remote_work_policy.md`: internal remote work policy.
- `data/source_documents/product_meeting_minutes.txt`: product meeting minutes.
- `data/source_documents/lumen_foundation_2025_activity_report.md`: a foundation's annual activity report.
- `data/example_prompts/prompt_v1.txt` and `prompt_v2.txt`: examples of summarization instructions to compare and evolve.
- `data/evaluation_sets/eval.csv`: documents and reference summaries to build and run your evaluation.

## Real-world constraints

- Content stays within the information system and must not be sent to an external service.
- Documents can be long and require processing whose duration varies.
- The user must understand the status of a job and be able to retrieve the result without an opaque wait.
- Modest machines may be used; plan for acceptable behavior when resources are limited or the service is unavailable.

## Current business workflows

### Requesting a document summary

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Document to read → employee → document, reading goal, confidentiality level → decide which type of summary is useful and which information to preserve → submit the request → summary suited to the reading need.

Observable friction and risks: ambiguous instruction, document too long, important information omitted, sensitive content exposed.

### Following a long-running job

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Request in progress → employee, internal service → job status, resource availability, document concerned → decide whether to wait, retry or reduce the scope of the request → check progress and retrieve the result when available → user informed without an opaque block.

Observable friction and risks: unpredictable duration, unreported failure, local unavailability, lost result.

### Sharing a sensitive summary

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Summary prepared for sharing → employee, team manager → source document, summary, recipients and confidentiality rules → verify accuracy and the authorized level of distribution → a human manager approves the sharing when the impact is sensitive → summary shared with authorized people, with the necessary caveats.

Observable friction and risks: inaccurate summary, omitted nuance, sharing with the wrong recipient, missing approval.

## Your framing

Based on these elements, choose a priority objective and formulate an observable MVP. Which precise problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric and the sources that are really useful. Specify the chosen level of automation, the risks, the safeguards and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the MVP genuinely helps without increasing risk?

Explicitly justify why a **simple LLM call (chat)**, a **Workflow**, a **RAG** or an **Agent** is retained or ruled out for your scope — the simplest solution that proves the value is a legitimate choice. Explain how you preserve confidentiality, evaluate quality and handle long or unavailable processing.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from framing to operations and recalls the expected software engineering good practices.

Document your important decisions in ADRs and keep the evidence requested at each phase: contract, baseline, tests, evaluation results, traces and demonstrations of operation or controlled failure.

The set of 5 to 10 cases required from the framing stage can start from the cases provided in `data/evaluation_sets/`; complete them with your own ambiguous and error cases, documenting what you add and why.
