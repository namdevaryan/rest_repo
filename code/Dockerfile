# Stage 1: Build dependencies in a temporary container
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies in a virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Final lightweight Flask image
FROM python:3.11-slim

WORKDIR /app

# Copy only installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application files
COPY main.py .

# Expose port
EXPOSE 8080

# Run Flask app
CMD ["python", "main.py"]
