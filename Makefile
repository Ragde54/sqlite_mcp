install:
	uv sync --group dev

test:
	uv run pytest tests/

lint:
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/

typecheck:
	uv run mypy src/

check: lint typecheck test

seed:
	uv run python scripts/seed.py
