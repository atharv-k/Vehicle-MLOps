<div align="center">

<br/>

```
██╗   ██╗███████╗██╗  ██╗██╗ ██████╗██╗     ███████╗
██║   ██║██╔════╝██║  ██║██║██╔════╝██║     ██╔════╝
██║   ██║█████╗  ███████║██║██║     ██║     █████╗  
╚██╗ ██╔╝██╔══╝  ██╔══██║██║██║     ██║     ██╔══╝  
 ╚████╔╝ ███████╗██║  ██║██║╚██████╗███████╗███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝╚══════╝
            M L O P S   P I P E L I N E
```

### End-to-End Machine Learning System for Vehicle Insurance Prediction

<br/>

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com/atlas)
[![AWS](https://img.shields.io/badge/AWS-S3_|_EC2_|_ECR-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

</div>

---

## 🧠 What This Project Does

A **production-grade MLOps pipeline** that automates the complete lifecycle of a machine learning model — from raw data ingestion through cloud deployment — with zero manual intervention. Built to mirror how ML systems operate at scale in industry.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        TRAINING PIPELINE                            │
│                                                                     │
│  MongoDB Atlas ──► Data Ingestion ──► Data Validation               │
│                                            │                        │
│                    Model Pusher ◄── Model Trainer ◄── Data Transform│
│                         │                                           │
│                    AWS S3 Bucket (Model Registry)                   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  PREDICTION API    │
                    │  FastAPI + Docker  │
                    │  EC2 (Port 5080)   │
                    └────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                        CI/CD PIPELINE                               │
│                                                                     │
│   GitHub Push ──► GitHub Actions ──► Docker Build ──► ECR Push      │
│                                                │                    │
│                         EC2 Self-Hosted Runner ◄── Pull & Deploy    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10 | Core development |
| **Environment** | Conda | Isolated virtual environment |
| **Database** | MongoDB Atlas | Cloud NoSQL data store |
| **Cloud Storage** | AWS S3 | Model registry & versioning |
| **Compute** | AWS EC2 (T2 Medium) | Production server |
| **Container Registry** | AWS ECR | Docker image storage |
| **Containerization** | Docker | Reproducible deployments |
| **CI/CD** | GitHub Actions | Automated pipeline |
| **API Framework** | FastAPI | Prediction & training endpoints |
| **Packaging** | setup.py + pyproject.toml | Local package management |

---

## 📦 Pipeline Components

### 1 · Data Ingestion
- Connects to **MongoDB Atlas** via secure connection string
- Fetches raw data in key-value format and transforms it into a structured DataFrame
- Outputs clean train/test splits as artifacts

### 2 · Data Validation
- Schema-driven validation using `config/schema.yaml`
- Checks column names, data types, and missing value thresholds
- Prevents corrupt data from propagating downstream

### 3 · Data Transformation
- Feature engineering pipelines with scikit-learn
- Handles categorical encoding, scaling, and imbalance
- Saves transformation objects for inference-time consistency

### 4 · Model Trainer
- Trains classification model on transformed data
- Evaluates against threshold metrics defined in constants
- Serializes best model using custom `NetworkModel` estimator

### 5 · Model Evaluation
- Compares newly trained model against the **production model on S3**
- Only promotes if improvement exceeds `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02`
- Prevents model degradation in production

### 6 · Model Pusher
- Pushes the accepted model to **AWS S3** model registry (`my-model-mlopsproj`)
- Tags model under `model-registry` key for versioned retrieval

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+, Conda
- MongoDB Atlas account
- AWS account (IAM user with AdministratorAccess)
- Docker installed locally

### 1 · Clone & Setup Environment

```bash
git clone https://github.com/your-username/vehicle-mlops.git
cd vehicle-mlops

conda create -n vehicle python=3.10 -y
conda activate vehicle

pip install -r requirements.txt
pip list  # verify local packages are installed
```

### 2 · Configure MongoDB

Sign up at [MongoDB Atlas](https://www.mongodb.com/atlas), create a free M0 cluster, and grab your connection string.

```bash
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"

# PowerShell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/"
```

> 📌 Allow access from `0.0.0.0/0` in MongoDB Network Access settings.

### 3 · Configure AWS Credentials

```bash
# Bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"

# PowerShell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
```

Create an S3 bucket named `my-model-mlopsproj` in `us-east-1` with public access enabled.

### 4 · Run Training Pipeline

```bash
python demo.py
```

### 5 · Launch Prediction API

```bash
python app.py
# Visit: http://localhost:5080
# Trigger training: http://localhost:5080/training
```

---

## 🔄 CI/CD Pipeline

The project includes a fully automated GitHub Actions workflow:

```
developer pushes code
        │
        ▼
GitHub Actions triggered
        │
        ├─► Build Docker image
        ├─► Push to AWS ECR
        └─► EC2 Self-Hosted Runner pulls & deploys
                    │
                    ▼
        App live on EC2:5080
```

### GitHub Secrets Required

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_DEFAULT_REGION` | `us-east-1` |
| `ECR_REPO` | ECR repository URI |

### EC2 Setup

```bash
# Install Docker on EC2
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

Connect EC2 as a GitHub self-hosted runner via:  
`GitHub Project → Settings → Actions → Runners → New self-hosted runner`

---

## 📁 Project Structure

```
vehicle-mlops/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/
│   │   ├── mongo_db_connections.py
│   │   └── aws_connection.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   │
│   ├── data_access/
│   ├── aws_storage/
│   ├── pipeline/
│   │   └── training_pipeline.py
│   ├── utils/
│   │   └── main_utils.py
│   └── constants/
│       └── __init__.py
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   └── mongoDB_demo.ipynb
│
├── config/
│   └── schema.yaml
│
├── static/
├── templates/
├── app.py
├── demo.py
├── Dockerfile
├── .github/workflows/aws.yaml
├── requirements.txt
├── setup.py
└── pyproject.toml
```

---

## 📊 Key MLOps Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Modular Pipelines** | Each ML step is an independent, testable component |
| **Artifact Tracking** | Every stage persists outputs as typed artifact objects |
| **Model Registry** | Versioned model storage on AWS S3 |
| **Model Gating** | Automated comparison before production promotion |
| **Reproducibility** | Docker containers ensure identical environments |
| **Automated Deployment** | Zero-touch deploy on every code push |
| **Environment Config** | All secrets managed via environment variables |
| **Schema Validation** | Data contracts enforced before training begins |

---

## 🪵 Logging & Exception Handling

- Centralized logger with timestamped outputs across all modules
- Custom exception handler with file name and line number tracing
- Tested independently before integration into pipeline components

---

<div align="center">

**Built with precision. Deployed with confidence.**

*If this project helped you, consider giving it a ⭐*

</div>
