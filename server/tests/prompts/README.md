# Prompt evaluations

Add prompt runs to `prompt_cases.yaml`. Each run contains:

- `target`: the import path and function, for example `prompts.text_quiz:get_text_quiz`
- `comment`: the code or prompt change being evaluated
- `args`: the complete keyword arguments for that function

Run the evaluations from `server` with:

```bash
python -m pytest tests/prompts/test_prompt_cases.py --run-prompts -q
```

Results are written after every run to a timestamped file such as
`tests/prompts/results/2026-09-18-14-30-00.yaml`. Each test result has only
`test`, `comments`, `results`, and `status` fields. Set `PROMPT_OUTPUT_FILE` to
use another output file. YAML comments beginning with `#` are copied to the
output header.