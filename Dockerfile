FROM python:3.12-alpine

WORKDIR /app

# Copy the entire project first so metadata can be generated
COPY . .

# Install the project and its dependencies
RUN pip install --no-cache-dir .

# The entry point 'thehouse' is created by the [project.scripts] in pyproject.toml
CMD ["thehouse"]
