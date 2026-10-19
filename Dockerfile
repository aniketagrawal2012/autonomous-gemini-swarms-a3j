# Google Cloud Vertex AI Enterprise Swarms & Graph-A3J Showcase
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    GOOGLE_GENAI_USE_VERTEXAI="true" \
    GOOGLE_CLOUD_PROJECT="aniket-personal" \
    GOOGLE_CLOUD_LOCATION="us-central1" \
    VERTEX_AI_MODEL="gemini-2.0-flash-001" \
    MPLCONFIGDIR="/tmp/matplotlib"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and assets
COPY . .

# Ensure tmp directories and static assets exist
RUN mkdir -p /tmp/matplotlib /app/static /app/artifacts

EXPOSE 8080

CMD ["python", "app_showcase.py"]
