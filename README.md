# Flask microservices

This project contains two independently runnable Flask microservices. Each service exposes one JSON API.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the services

In separate terminals:

```bash
python service_one/app.py
python service_two/app.py
```

## APIs

| Service | Method | URL |
| --- | --- | --- |
| Service one | `GET` | `http://localhost:5001/api/greeting` |
| Service two | `GET` | `http://localhost:5002/api/status` |

Example requests:

```bash
curl http://localhost:5001/api/greeting
curl http://localhost:5002/api/status
```

## Run with Docker Compose

Build and start both services:

```bash
docker compose up --build
```

Each service can also be built independently from its own directory:

```bash
docker build -t service-one:latest ./service_one
docker build -t service-two:latest ./service_two
```

Stop the services:

```bash
docker compose down
```