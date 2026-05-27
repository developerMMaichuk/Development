# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository nature

This is a personal learning sandbox, not a coherent application. It contains:

- Loose, standalone Python scripts at the repo root exploring the Anthropic Python SDK (sync, async, streaming) and basic Python I/O.
- `mockdata/` — intended location for sample data files referenced by scripts (currently empty in the working tree).
- `kodekloud/Claude-Code-Reviewing-Prompts/` — a nested third-party git repository of markdown review prompts (Code Quality, Security). It is *content*, not code, and has its own `.git`; do not stage edits there as part of this repo's commits.

There is no build system, dependency manifest, lint config, or test suite. Don't add one unless asked.

## Running things

Scripts are run individually with the interpreter — there is no entry point or task runner.

```powershell
python .\firstclaudecall.py
python .\firstclaudeasynccall.py
python .\claudestreamcall.py
python .\read_members.py
```

The Anthropic scripts require `anthropic` installed (`pip install anthropic`) and the `ANTHROPIC_API_KEY` environment variable set — the SDK reads it automatically, so no key handling code is needed in new scripts.

`myfirstclaudemessageobject.py` is a reference snippet, **not** a runnable program — it accesses a `message` variable that is never defined in the file. Treat it as documentation of the `anthropic.types.Message` shape.

## Conventions to preserve

- **Model ID**: existing scripts use `claude-sonnet-4-6`. Keep that or use a current model ID (e.g. `claude-opus-4-7`, `claude-haiku-4-5-20251001`) — do not regress to older versions like `claude-3-*` or `claude-sonnet-4-20250514`.
- **Client construction**: rely on the implicit `ANTHROPIC_API_KEY` env-var pickup (`anthropic.Anthropic()` / `anthropic.AsyncAnthropic()`); don't introduce explicit key passing.
- **Path handling**: `read_members.py` uses `Path(__file__).parent / "mockdata" / ...`. Follow this anchored-to-script-file pattern for any new data-reading script so it works regardless of the caller's CWD.
- The CSV path in `read_members.py` is literally `members.csv.csv` (double extension). That's the expected filename; don't "fix" it without confirming.

## Platform notes

Primary environment is Windows + PowerShell. Use PowerShell syntax for shell examples (e.g. `$env:ANTHROPIC_API_KEY = "..."`, not `export`).
