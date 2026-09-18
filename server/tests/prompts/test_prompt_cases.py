import asyncio
import os
from datetime import datetime, timezone
from importlib import import_module
from pathlib import Path

import pytest
import yaml


CASES_FILE = Path(__file__).with_name("prompt_cases.yaml")
OUTPUT_FILE = os.environ.get("PROMPT_OUTPUT_FILE")


def _load_cases():
    with CASES_FILE.open(encoding="utf-8") as input_file:
        document = yaml.safe_load(input_file) or {}

    cases = document.get("runs", [])
    if not cases:
        raise ValueError(f"No runs found in {CASES_FILE}")
    return document, cases


def _input_comments():
    comments = []
    for line in CASES_FILE.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("#"):
            comments.append(line)
    return comments


def _write_results(results, output_file):
    output_file.parent.mkdir(parents=True, exist_ok=True)
    header = "\n".join(_input_comments())
    output = {
        "tests": results,
    }
    with output_file.open("w", encoding="utf-8") as output_file:
        if header:
            output_file.write(f"{header}\n\n")
        yaml.safe_dump(output, output_file, sort_keys=False, allow_unicode=True)


@pytest.mark.prompt_live
def test_prompt_cases(request):
    if not request.config.getoption("--run-prompts"):
        pytest.skip("Pass --run-prompts to run live prompt evaluations")

    _, cases = _load_cases()
    output_file = Path(OUTPUT_FILE) if OUTPUT_FILE else (
        CASES_FILE.parent
        / "results"
        / f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.yaml"
    )
    results = []
    failures = []

    for case in cases:
        result = {
            "test": {
                "target": case["target"],
                "params": case["args"],
            },
            "comments": case.get("comment", ""),
        }
        try:
            value = asyncio.run(_call_prompt_async(case["target"], case["args"]))
            result["results"] = value.model_dump(mode="json")
            result["status"] = "success"
        except Exception as error:  # Keep earlier model results when one run fails.
            result["results"] = {"error": f"{type(error).__name__}: {error}"}
            result["status"] = "fail"
            failures.append(case["name"])
        results.append(result)
        _write_results(results, output_file)

    assert not failures, f"Prompt runs failed: {', '.join(failures)}"


async def _call_prompt_async(target, arguments):
    module_name, function_name = target.split(":", maxsplit=1)
    function = getattr(import_module(module_name), function_name)
    return await function(**arguments)