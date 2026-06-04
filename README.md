# Practical MLOps

![Python CI](https://github.com/TBlair24/mlops/actions/workflows/main.yml/badge.svg)

A production-grade CI/CD pipeline built as part of the exercises from
[Practical MLOps](https://www.oreilly.com/library/view/practical-mlops/9781098103002/)
by Noah Gift and Alfredo Deza (O'Reilly).

---

## Project Overview

This project demonstrates end-to-end MLOps best practices including automated
testing, linting, containerisation, cloud-native CI, and load testing. A simple
Flask API serves as the application under test.

### API Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /` | Home — lists available endpoints | `curl http://127.0.0.1:8080/` |
| `GET /add` | Add two numbers | `curl "http://127.0.0.1:8080/add?x=5&y=3"` |
| `GET /subtract` | Subtract two numbers | `curl "http://127.0.0.1:8080/subtract?x=10&y=4"` |
| `GET /multiply` | Multiply two numbers | `curl "http://127.0.0.1:8080/multiply?x=6&y=7"` |

---

## Project Structure

```
mlops/
├── .github/
│   └── workflows/
│       ├── main.yml              # CI on main (GitHub Actions)
│       └── staging.yml           # Load tests on staging branch
├── .dockerignore
├── Dockerfile                    # Container build
├── Makefile                      # Central build tool
├── buildspec.yml                 # AWS CodeBuild config
├── app.py                        # Flask API
├── hello.py                      # Core functions
├── test_hello.py                 # Unit tests
├── locustfile.py                 # Load test definition
├── run_loadtest.sh               # Load test runner
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- Docker
- AWS CLI (for ECR and CodeBuild)

### Installation

```bash
# Clone the repo
git clone https://github.com/TBlair24/mlops.git
cd mlops

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
make install
```

### Run Locally

```bash
python app.py
```

The API will be available at `http://127.0.0.1:8080`.

---

## Makefile Targets

| Command | Description |
|---------|-------------|
| `make install` | Install all dependencies |
| `make lint` | Run pylint on source code |
| `make format` | Auto-format code with Black |
| `make test` | Run unit tests with pytest and coverage |
| `make loadtest` | Run Locust load test against the API |
| `make all` | Run install, lint, format, and test |

---

## CI/CD Pipeline

### GitHub Actions (main branch)

Triggers on every push to `main`. Tests across Python 3.9, 3.10, and 3.11 in
parallel.

- Install dependencies
- Lint with pylint
- Format check with Black
- Unit tests with pytest

### GitHub Actions (staging branch)

Triggers on every push to `staging`. Runs the full CI pipeline plus an
automated load test using Locust.

### AWS CodeBuild

Triggers on every push via webhook. Runs linting, format checking, unit tests,
builds the Docker image, and pushes it to Amazon ECR.

---

## Docker

### Build and Run

```bash
# Build the image
docker build -t mlops .

# Run the container
docker run -d -p 8080:8080 --name mlops-app mlops

# Test it
curl http://127.0.0.1:8080/

# Stop and remove
docker stop mlops-app && docker rm mlops-app
```

### Push to Amazon ECR

```bash
aws ecr get-login-password --region eu-north-1 | \
    docker login --username AWS --password-stdin \
    568256617374.dkr.ecr.eu-north-1.amazonaws.com

docker tag mlops:latest \
    568256617374.dkr.ecr.eu-north-1.amazonaws.com/mlops:latest

docker push \
    568256617374.dkr.ecr.eu-north-1.amazonaws.com/mlops:latest
```

---

## Load Testing

Load tests use [Locust](https://locust.io/) to simulate concurrent users
hitting the API.

### Run Manually

```bash
# Terminal 1: Start the app
python app.py

# Terminal 2: Run load test
locust -f locustfile.py \
    --host=http://127.0.0.1:8080 \
    --headless \
    --users 10 \
    --spawn-rate 2 \
    --run-time 30s
```

---

## Exercises Completed

| # | Exercise | Tools Used |
|---|----------|------------|
| 1 | Python scaffold with Makefile, linting, testing | Makefile, pylint, Black, pytest |
| 2 | GitHub Actions with multiple Python versions | GitHub Actions, Python 3.9/3.10/3.11 |
| 3 | Cloud-native CI | AWS CodeBuild |
| 4 | Containerisation with automatic registry push | Docker, Amazon ECR |
| 5 | Automated load testing on staging branch | Locust, GitHub Actions |

---

## References

- [Practical MLOps – O'Reilly](https://www.oreilly.com/library/view/practical-mlops/9781098103002/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [AWS CodeBuild Documentation](https://docs.aws.amazon.com/codebuild/)
- [Locust Documentation](https://docs.locust.io/)
