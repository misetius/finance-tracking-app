# Finance Tracking App

A full-stack finance tracking application built with **Flask** (backend) and **React** (frontend).  
This project is created for learning purposes, with a focus on practicing **Docker** and **Kubernetes** deployment.

---


You can quickly try the app with docker compose file. For this you obviously need to have installed docker.

You can run this file with command while in the same directory as the file on the command line:

```
docker compose up
```

After this you can access the app from localhost with the browser


---

##  Overview

Finance Tracking App allows users to:

- Track income and expenses
- Categorize transactions
- View financial summaries


The application is fully containerized and deployed to Kubernetes as part of DevOps practice.

---

## Tech Stack

### Backend
- Flask (Python)
- REST API
- PostgreSQL

### Analytics
- Flask (Python)
- REST API
- PostgreSQL

### Frontend
- React
- Axios
- Component-based architecture

### 

### DevOps / Infrastructure
- Docker
- Kubernetes
- Kubernetes Secrets
- Deployment & Service manifests

---
Note: The analytics service is included **purely for Kubernetes and microservices practice purposes**.

In a real-world application of this size, the analytics logic (such as average calculations) would typically be implemented directly inside the main backend service. Creating a separate container for this functionality would be unnecessary and would add extra complexity.

However, in this project the analytics service exists to:

- Practice multi-container application architecture
- Learn Kubernetes Service-to-Service communication
- Experiment with scaling independent services
- Understand microservice-style deployment patterns

The frontend communicates only with the main backend service.  
The backend then communicates internally with the analytics-service within the Kubernetes cluster.
