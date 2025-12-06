# Dockerfile for Railway deployment
# This works when Root Directory is NOT set (builds from root)
# If Root Directory IS set to 'backend', Railway will use backend/Dockerfile instead

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy backend dependency files
COPY backend/pyproject.toml backend/requirements.txt ./

# Copy backend application code (needed for editable install)
COPY backend/ .

# Install Python dependencies (after code is copied)
RUN pip install --no-cache-dir -e .

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

