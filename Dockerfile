FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy project files
COPY . .

# Install the project and its dependencies
RUN uv sync --frozen --no-dev

# The entry point 'thehouse' is created by the [project.scripts] in pyproject.toml
CMD ["uv", "run", "thehouse"]
