# ---- Stage 1: builder ----
FROM ghcr.io/astral-sh/uv:python3.12-slim AS builder

WORKDIR /app

# Enable bytecode compilation and set venv path
ENV UV_COMPILE_BYTECODE=1
ENV VIRTUAL_ENV=/app/.venv

# Copy project files
COPY pyproject.toml uv.lock README.md ./

# Copy source code
COPY src/ ./src/

# Install dependencies and the project
RUN uv sync --frozen --no-dev --no-editable

# ---- Stage 2: final ----
FROM python:3.12-slim AS final

WORKDIR /app

RUN groupadd --gid 1001 appgroup && \
    useradd --uid 1001 --gid appgroup --shell /bin/bash --create-home appuser

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY alembic/ ./alembic/
COPY alembic.ini ./
COPY entrypoint.sh ./

RUN mkdir -p /app/data && \
    chown appuser:appgroup /app/data && \
    chmod +x entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src"
ENV DATABASE_URL="sqlite:////app/data/habit_tracker.db"

USER appuser

ENTRYPOINT ["./entrypoint.sh"]
