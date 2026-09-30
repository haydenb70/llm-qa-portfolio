# LLM QA Portfolio

Quality testing for an AI product-support chatbot, built by a QA engineer with a Selenium and regulated banking background.

## What this project tests

A small retrieval (RAG) chatbot answers customer questions using product information from a water filtration store. The test suite checks whether the bot:

- Answers only from the product information it was given
- Refuses to make health or medical claims the source does not support
- Admits when it does not know, instead of inventing specs
- Resists prompt injection (users trying to override its instructions)

Wrong answers here are not just bugs. Overstated claims about what a water filter removes are a real safety and legal risk, which is why this project treats them like high-severity defects.

## Status

| Phase | Goal | Status |
| --- | --- | --- |
| 1 | First 5 eval cases running locally with Promptfoo | In progress |
| 2 | 30+ eval cases covering accuracy, refusals, and injection | Not started |
| 3 | Evals run automatically in GitHub Actions on every change | Not started |
| 4 | Red-team report written up like a defect report | Not started |
| 5 | Playwright end-to-end tests against a chat UI | Not started |

## Tech

- Python 3.11+ and pytest
- [Promptfoo](https://www.promptfoo.dev/) for LLM evals
- [Ollama](https://ollama.com) for running a local model at no cost

## Run it locally

```bash
# 0. Check the source data with pytest (no model needed)
python3 -m pip install -r requirements.txt
python3 -m pytest -v

# 1. Install Promptfoo (needs Node.js 20+)
npm install -g promptfoo

# 2. Install Ollama, then pull a small local model
ollama pull llama3.2

# 3. Run the evals and open the results viewer
promptfoo eval -c evals/promptfooconfig.yaml
promptfoo view
```

## Repo layout

```
tests/        pytest checks on the source data
evals/        Promptfoo config and test cases
data/         Product information the chatbot answers from
docs/         Test strategy and findings reports
```

## About

Built by Hayden Dennis as part of a move from traditional QA into AI and LLM testing.
LinkedIn Profile: linkedin.com/in/haydenbdennis/