# AIRIA — Data Analytics Agent recommended settings

Use these alongside [prompts/DATA_ANALYTICS_AGENT_COMBINED_PDF_AND_CSV.md](../prompts/DATA_ANALYTICS_AGENT_COMBINED_PDF_AND_CSV.md) when the agent must return **one response** containing a **PDF-ready report** plus **two machine-parseable CSV blocks**.

Settings are tuned for **format stability** (CSV markers and headers) while keeping enough latitude for narrative in PART 1.

---

## Model

| Setting | Recommendation | Why |
|--------|----------------|-----|
| **Model** | **Claude Sonnet 4.6** (`claude-sonnet-4-6`) | Matches your Team 2 architecture diagram; strong at structured long outputs. |
| **Alternatives** | Sonnet-class only for production; cheaper models OK for early **marker** experiments | Flash/Gemini can work for format drills but often diverges on long reports + CSV in one shot. |

---

## Sampling and reasoning

| Setting | Recommendation | Why |
|--------|----------------|-----|
| **Temperature** | **0.25–0.35** (start **0.3**) | Lower randomness reduces markdown fences, renamed columns, and “creative” CSV. **Avoid 0.7** for this agent. |
| **Reasoning effort** | **Balanced** | **Fast** if latency matters and inputs are small; **Deep** only if you see logic errors in trend math (adds latency). |

---

## Context toggles (AIRIA “Model” tab)

| Toggle | Recommendation | Why |
|--------|----------------|-----|
| **Date and time context** | **On**, timezone **UTC** | Helps period boundaries (daily/weekly/monthly) and consistent `due_date` reasoning; state “as of” in PART 1. |
| **User details context** | **Off** | Reduces irrelevant personalization tokens in a batch analytics step. |
| **Always include user input** | **On** (if your graph passes batch via user/input node) | Ensures the merged RYS/Zendesk payload reaches the agent even when the step is not the only predecessor. |

---

## Tools / MCP

| Area | Recommendation |
|------|----------------|
| **Tools** | None required for text report + CSV strings. Add only if AIRIA requires a specific **export** or **file** tool for attachments. |
| **MCP** | Only if your tenant uses MCP for PDF or storage; otherwise leave off to reduce failure modes. |

---

## Operational tips

1. **If PART 2 fails validation** — drop temperature further (e.g. **0.2**) and add one line to the prompt: “If you cannot fit PART 1 in one message, shorten PART 1 tables but never omit PART 2.”
2. **If PART 1 is too long** — tighten “Detailed tables” to one window (e.g. weekly only) in the prompt for demo runs.
3. **Attachment step** — downstream should **split** on the four marker lines; do not ask the email model to “regenerate” CSV.

---

## Quick copy block (for lab notes)

```
Model:     Claude Sonnet 4.6
Temp:      0.3
Reasoning: Balanced
Date/time: On, UTC
User ctx:  Off
User in:   On (if batch comes from input)
```
