# Dan's Crew AI template

Inspired by [crew-ai-crash-course](https://github.com/bhancockio/crew-ai-crash-course) with added README and use of [UV](https://docs.astral.sh/uv)

How to set up UV with just the poetry pyproject.toml file. We migrate the poetry file first.

```bash
brew install uv
uvx pdm import pyproject.toml
uv pip install .
uv lock
```

Install new packages with UV

```bash
uv add pytest
```