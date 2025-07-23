FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    poppler-utils && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV RUNNING_IN_DOCKER=true

VOLUME ["/app/input", "/app/output"]

ENTRYPOINT ["python", "main.py"]