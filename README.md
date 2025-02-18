# Dan's Crew AI template

Inspired by [crew-ai-crash-course](https://github.com/bhancockio/crew-ai-crash-course), this repo is designed 
to showcase some simple examples of agents, tasks and custom tools that can be used as a starting point
for your Crew AI project.

This project uses [UV](https://docs.astral.sh/uv), which used a migrated poetry file. This is how the migrations was
done:

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