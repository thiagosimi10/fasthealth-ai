# 🚀 FastHealth AI – Scalable Health Risk Prediction API

**FastHealth AI** is a high-performance, AI-powered backend service built with **FastAPI**, **PostgreSQL**, **Redis**, and **Docker**.  
It enables real-time predictions of patient health risks (e.g., hypertension, diabetes) through RESTful APIs, using pre-trained machine learning models.

This project demonstrates modern backend architecture, asynchronous data handling, caching strategies, and containerized infrastructure — all production-ready and cloud-deployable.

---

## 🧠 System Overview

### 📍 Purpose
FastHealth AI was designed to simulate a real-world microservice capable of:
- Receiving **patient clinical data** (vitals, symptoms)
- Processing it via **AI models**
- Responding instantly with **risk classifications**
- Storing results in a relational database
- Exposing clean, documented, and versioned **REST APIs**

### 🔁 Data Flow

```
[Client App]
     |
     ↓
[FastAPI REST API] → [ML Model Prediction] → [PostgreSQL/Redis Storage]
     ↑
     └──── Swagger Docs, Auth, Monitoring
```

---

## 🛠️ Tech Stack

| Layer        | Tool                 | Purpose                            |
|--------------|----------------------|------------------------------------|
| Backend API  | FastAPI (async)      | REST endpoints, validation, docs   |
| ML Engine    | Scikit-learn         | Risk prediction models             |
| Database     | PostgreSQL           | Persistent patient data storage    |
| Cache        | Redis                | Fast metrics & prediction caching  |
| ORM          | SQLAlchemy 2.0 (async)| DB modeling & async query engine  |
| Container    | Docker & Docker Compose | Isolation & orchestration        |
| Tests        | Pytest               | Automated testing framework        |
| Docs         | OpenAPI / Swagger    | Auto-generated API documentation   |

---

## 📁 Project Structure

```
fasthealth-ai/
├── app/
│   ├── api/               # Route definitions
│   ├── core/              # Config, logging, security
│   ├── models/            # SQLAlchemy models
│   ├── services/          # Business logic (ML, caching)
│   ├── schemas/           # Pydantic models (request/response)
│   ├── tests/             # Pytest test suites
│   └── main.py            # App entry point
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Key Features

- ✅ FastAPI with async I/O for ultra-fast request handling
- ✅ Redis caching layer for reduced DB load and response times
- ✅ PostgreSQL for persistent, ACID-compliant data storage
- ✅ ML predictions served in real-time with scikit-learn
- ✅ Typed request/response validation via Pydantic
- ✅ Swagger UI available at `/docs`
- ✅ Containerized with Docker for easy deployment
- ✅ Fully testable via Pytest

---

## 🚀 Getting Started Locally

### 🔧 Requirements
- Docker
- Docker Compose
- Git

### 📦 Clone the project
```bash
git clone https://github.com/thiagosimi10/fasthealth-ai.git
cd fasthealth-ai
```

### ▶️ Start services
```bash
docker-compose up --build
```

- FastAPI API will be available at: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

### 🧪 Run tests
```bash
docker-compose exec api pytest
```

---

## 🔄 API Endpoints

| Method | Endpoint           | Description                          |
|--------|--------------------|--------------------------------------|
| POST   | `/predict-risk`    | Submit patient data for prediction   |
| GET    | `/patients`        | List all patients                    |
| GET    | `/patients/{id}`   | Get a specific patient record        |
| POST   | `/patients`        | Create a new patient record          |
| GET    | `/metrics`         | View cached prediction stats         |

All endpoints are documented in real time under `/docs`.

---

## 🧠 Sample Prediction Input

```json
{
  "age": 56,
  "gender": "male",
  "heart_rate": 92,
  "blood_pressure": 145,
  "glucose": 118,
  "symptoms": ["headache", "dizziness"]
}
```

---

## ☁️ Cloud Deployment (optional)

This project is structured to easily deploy on:

- AWS EC2 (via Docker)
- AWS Lambda + API Gateway (via FastAPI + Mangum)
- Fargate (with ECS + RDS + ElastiCache)

> Future versions may include Terraform/Ansible support and CI/CD pipelines via GitHub Actions.

---

## 📌 Future Enhancements

- ✅ Authentication with JWT
- ✅ Kafka integration for event streaming
- ✅ Prometheus metrics + Grafana dashboards
- ✅ Admin dashboard (React)
- ✅ Auto-scaling config for AWS ECS

---

## 👨‍💻 Author

Developed by **Thiago Simionato da Silva**, Senior Software Engineer  
🇧🇷 Based in Brazil | 💼 Targeting international remote positions  

> Want to collaborate or hire? Feel free to open an issue or contact me on [LinkedIn](https://www.linkedin.com/in/thiago-simionato-da-silva-4b558ab2)

---

## 📝 License

MIT License.  
Free to use, clone, and adapt — credits appreciated.
