FROM python:3.11-slim

# system deps (important for requests, SSL, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY app ./app

ENV PYTHONUNBUFFERED=1

# default command
CMD ["python", "-m", "app.main"]