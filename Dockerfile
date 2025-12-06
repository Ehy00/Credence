# Dockerfile for Railway deployment (at root)
# Railway will use this when Root Directory is NOT set to backend
# If Root Directory IS set to backend, Railway will use backend/Dockerfile instead

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files from backend
COPY backend/pyproject.toml backend/requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Copy application code from backend
COPY backend/ .

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

