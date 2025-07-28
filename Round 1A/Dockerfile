FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Install required system packages (minimal set for PyMuPDF)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to use Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code (including src directory)
COPY . .

# Make sure input/output folders are created
RUN mkdir -p /app/input /app/output

# Environment variable
ENV RUNNING_IN_DOCKER=true

# Run the processor
CMD ["python", "main.py"]