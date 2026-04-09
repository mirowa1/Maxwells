# KOA CIS 8396 — Data Analytics outputs (Team 2)

Canonical path: **`projects/koa-cis8396-csv/`** (commit this folder to GitHub).

## Layout

| Folder | Contents |
|--------|----------|
| [prompts/](prompts/) | Agent instructions to paste into AIRIA |
| [settings/](settings/) | Recommended model and context toggles |
| [tools/](tools/) | Validate output; split CSV blocks into `.csv` files |
| [data/](data/) | Synthetic input CSV exported from class sample reviews |
| [fixtures/](fixtures/) | Sample combined output for testing the validator |

## Primary files

- **One-response prompt (PDF report + two CSV blocks):** [prompts/DATA_ANALYTICS_AGENT_COMBINED_PDF_AND_CSV.md](prompts/DATA_ANALYTICS_AGENT_COMBINED_PDF_AND_CSV.md)
- **AIRIA settings:** [settings/AIRIA_DATA_ANALYTICS_RECOMMENDED_SETTINGS.md](settings/AIRIA_DATA_ANALYTICS_RECOMMENDED_SETTINGS.md)

## Validation

```bash
python3 projects/koa-cis8396-csv/tools/validate_csv_output.py projects/koa-cis8396-csv/fixtures/sample_combined_output.txt
```

## Split into two files (for manual email tests)

```bash
python3 projects/koa-cis8396-csv/tools/split_agent_output_to_csv.py run_output.txt ./email_attachments/
```
