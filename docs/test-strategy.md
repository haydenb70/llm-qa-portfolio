# Test strategy: product support chatbot

## Risk ranking

| Risk | Example failure | Severity |
| --- | --- | --- |
| Unsupported health or contaminant claims | "This filter removes lead" when it is not certified to | Critical |
| Prompt injection | User talks the bot into making false claims | High |
| Invented facts | Making up a price, spec, or warranty term | High |
| Wrong facts from the source | Misstating filter life or return window | Medium |
| Unhelpful refusals | Refusing questions the source can answer | Low |

## Approach

- Deterministic checks first (text must or must not appear), because they are cheap, fast, and repeatable.
- Model-graded checks (LLM-as-judge) later, for answers that can be correct in many different wordings.
- Every eval case maps to one risk above, the same way a test case maps to a requirement.

## Open questions

- Which real product page and FAQ to use as the source data
- Which model to test against beyond the local model
