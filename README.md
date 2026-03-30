-----

# 🚀 Vehicle Data Intelligence: End-to-End MLOps Pipeline

[](https://www.python.org/)
[](https://www.mongodb.com/)
[](https://aws.amazon.com/)
[](https://www.docker.com/)
[](https://github.com/features/actions)

## 📌 Project Overview

This project demonstrates a production-grade MLOps ecosystem designed to automate the lifecycle of a machine learning model. From **Agentic Data Ingestion** using MongoDB to **Cloud-Native Deployment** on AWS, every stage is orchestrated to ensure scalability, observability, and reproducible results.

[Image of MLOps lifecycle diagram]

### 🛠 Tech Stack & Services

  * **Infrastructure:** AWS (S3 for Model Registry, ECR for Container Storage, EC2 for Deployment).
  * **Database:** MongoDB Atlas (NoSQL storage for raw and transformed datasets).
  * **Orchestration:** Custom Multi-Agent workflows using `setup.py` and `pyproject.toml` for local package management.
  * **CI/CD:** GitHub Actions with Self-Hosted Runners on Ubuntu instances.
  * **Monitoring:** Integrated Logging and Custom Exception Handling across all modules.

-----

## 🏗 System Architecture

The pipeline is divided into modular components to ensure clean separation of concerns:

1.  **Data Ingestion:** Fetches data from MongoDB Atlas, converts Key-Value pairs to Dataframes, and stores them as artifacts.
2.  **Data Validation:** Validates data drift and schema integrity using `config.schema.yaml`.
3.  **Data Transformation:** Feature engineering and preprocessing using specialized estimators.
4.  **Model Trainer:** Trains the model and exports serialized artifacts.
5.  **Model Evaluation & Pusher:** Compares new models against a threshold score; if successful, pushes the model to the AWS S3 Model Registry.

-----

## 🚀 Getting Started

### 1\. Environment Setup

```bash
# Create and activate environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# Install dependencies
pip install -r requirements.txt
```

### 2\. Configuration (Environment Variables)

To connect the local pipeline to Cloud Services, set the following secrets in your environment:

| Variable | Description |
| :--- | :--- |
| `MONGODB_URL` | MongoDB Atlas Connection String |
| `AWS_ACCESS_KEY_ID` | AWS IAM User Access Key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM User Secret Key |
| `AWS_DEFAULT_REGION` | Set to `us-east-1` |

-----

## 📦 Infrastructure & Deployment

### Dockerization

The application is containerized to ensure "Run Anywhere" capability.

```bash
docker build -t vehicle-app .
docker run -p 5080:5080 -e MONGODB_URL="..." vehicle-app
```

### CI/CD Workflow (GitHub Actions)

The project utilizes a self-hosted runner on **AWS EC2 (T2 Medium)**.

1.  **Continuous Integration:** Triggered on every push; builds the Docker image and pushes it to **AWS ECR**.
2.  **Continuous Deployment:** Pulls the latest image from ECR to the EC2 instance and launches the container.

-----

## 📊 Usage

  * **Web Interface:** Access the application at `http://<EC2-Public-IP>:5080`
  * **Training Pipeline:** Trigger a fresh model training at `/training`
  * **Prediction:** Use the UI to submit vehicle data for real-time inference.

-----

## 📁 Project Structure

```text
├── .github/workflows   <- CI/CD pipeline definitions
├── components          <- Data Ingestion, Validation, Transformation, etc.
├── configuration       <- AWS & MongoDB connection logic
├── entity              <- Config and Artifact entities
├── notebook            <- EDA and Feature Engineering experiments
├── static/templates    <- Web UI assets
├── app.py              <- Main Application Entry Point
└── setup.py            <- Local package distribution
```

-----
