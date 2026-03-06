FROM python:3.12-alpine

WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir .

# Copy the source code
COPY thehouse ./thehouse

# Set version (optional, but good for metadata)
ENV PYTHONPATH=/app

CMD ["python", "-m", "thehouse"]
