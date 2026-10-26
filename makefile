run:
	uv run fastapi dev  --reload

format:
	uv run ruff check --fix --unsafe-fixes
	uv run ruff format

check:
	uv run ruff check --fix