# Contributing

Thanks for helping improve Is On Water. Keep changes focused, documented, and
easy to verify.

## Local setup

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
```

Install the required ASTWBD archives from
[`is-on-water-dataset`](https://github.com/auroravicks/is-on-water-dataset).

## Before opening a pull request

```bash
ruff check .
ruff format --check .
python -m compileall -q main.py water.py
```

For API integration checks, start `uvicorn main:app` in one terminal and run
`pytest` in another. Describe any dataset-dependent behavior you tested in the
pull request.

Please avoid committing generated artifacts, local environments, or unrelated
dataset changes.
