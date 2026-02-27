# 🐳 Docker ML Lab – From Scratch

## 📌 Overview

This lab demonstrates how to containerize a Machine Learning training pipeline using Docker.

I built a complete ML training workflow from scratch, packaged it into a Docker image, and executed it inside a container to ensure reproducibility and portability.

This lab demonstrates key Docker and MLOps concepts:
- Dockerfile creation
- Image building
- Container execution
- Dependency management
- Reproducible ML environments

---

# 🧠 What is Docker?

Docker is a containerization platform that allows applications and their dependencies to be packaged into lightweight, portable containers.

A Docker container ensures:
- Same Python version everywhere
- Same library versions
- Same system dependencies
- Reproducible execution

Think of it as a box that contains everything needed to run the project.

---

# 🤖 Why Docker is Important in MLOps

In Machine Learning projects, issues commonly occur due to:

- Different Python versions
- Different scikit-learn versions
- Missing dependencies
- "Works on my machine" problems

Docker solves these by:

- Packaging code + dependencies together
- Creating reproducible ML environments
- Simplifying deployment
- Enabling scalable production workflows

---

# 🏗 What I Built in This Lab

I created:

- A Machine Learning training script
- A Dockerfile to define the environment
- A Docker image containing the ML setup
- A Docker container that executes the training

The script:

- Loads the Wine dataset (scikit-learn)
- Splits the dataset
- Trains a Logistic Regression model
- Evaluates model accuracy
- Saves the trained model as `wine_model.pkl`

---

# 📂 Project Structure

docker-ml-lab/
│
├── Dockerfile
├── src/
│   ├── main.py
│   └── requirements.txt
└── README.md

---

# 🧪 Machine Learning Implementation Details

Dataset Used:
- Wine Dataset (from scikit-learn)

Model Used:
- Logistic Regression

Evaluation Metric:
- Accuracy Score

Model Output:
- Saved as `wine_model.pkl`

---

# 🐳 Docker Implementation Steps

## Step 1 – Build Docker Image

From the project root directory:

```bash
docker build -t docker-ml-lab:v1 .
```

What this does:

- Downloads Python 3.10 base image
- Copies source code into container
- Installs required dependencies
- Creates a reusable Docker image

---

## Step 2 – Run Docker Container

```bash
docker run docker-ml-lab:v1
```

Expected Output:

Model training completed successfully.
Model accuracy: 0.9X

This confirms:

- Code runs inside container
- Dependencies installed correctly
- Model training successful

---

## Step 3 – View Docker Images

```bash
docker images
```

---

## Step 4 – View Containers

```bash
docker ps -a
```

---

# 🧱 Dockerfile Explanation

Dockerfile used in this project:

```dockerfile
FROM python:3.10
WORKDIR /app
COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```
Explanation:

- FROM → Base Python image
- WORKDIR → Sets working directory inside container
- COPY → Copies source files into container
- RUN → Installs dependencies
- CMD → Executes training script when container starts

---
# 🔄 How This Demonstrates MLOps

This lab demonstrates:

- Environment reproducibility
- Dependency isolation
- Containerized ML training
- Image versioning
- Portable ML workflows

The trained model can now be:

- Deployed to cloud
- Used in CI/CD pipelines
- Integrated into model serving APIs

---

# 🔄 Modifications for Originality

To ensure originality and avoid identical implementation:

- Used Wine dataset instead of Iris
- Used Logistic Regression instead of RandomForest
- Added accuracy evaluation metric
- Changed model output filename
- Built project completely from scratch

---

# 🏁 Final Summary

This lab successfully demonstrates how to containerize a machine learning training workflow using Docker, ensuring reproducibility, portability, and deployment readiness — key principles in modern MLOps practices.
