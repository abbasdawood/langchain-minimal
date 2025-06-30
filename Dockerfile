FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 65432

# Set environment variable for the port
ENV PORT=65432

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "65432"]