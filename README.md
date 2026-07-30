# Cloud Document Management System

A backend API for a cloud-based document management system built with **FastAPI**, **PostgreSQL**, and **AWS S3**.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Passlib (bcrypt)
* AWS S3
* Boto3
* Python 3.12

---

## Phase 1: Authentication (Completed)

### Project Setup

* FastAPI project structure
* Environment variables (`.env`)
* PostgreSQL database
* SQLAlchemy ORM
* Alembic migrations

### User System

* User model
* Password hashing
* User registration
* User login

### Authentication

* JWT token generation
* JWT validation
* Protected routes
* Current authenticated user endpoint

### API Endpoints

* `POST /auth/register`
* `POST /auth/login`
* `GET /users/me`

---

## Phase 2: Document Management (Completed)

### Document System

* Document model
* File upload
* File metadata storage
* Associate documents with users
* List user documents
* Download documents
* Delete documents
* User authorization

### API Endpoints

* `POST /documents/upload`
* `GET /documents`
* `GET /documents/{document_id}`
* `DELETE /documents/{document_id}`

---

## Phase 3: Cloud Storage (AWS S3) (Completed)

### AWS Integration

* AWS S3 bucket
* IAM user and access keys
* Boto3 integration
* Upload files to AWS S3
* Download files from AWS S3
* Delete files from AWS S3
* Store S3 object keys in PostgreSQL

---

## Phase 4: Docker (Completed)

### Containerization

- Dockerized FastAPI application
- Dockerized PostgreSQL database
- Docker Compose orchestration
- Persistent PostgreSQL volumes
- Health checks for database startup
- Environment variable management

---

## Future Improvements

* Docker
* Redis caching
* Background tasks
* Email verification
* Password reset
* CI/CD
* Deployment
* React frontend
* Unit and integration tests

---

## Progress

- [x] Phase 1 – Authentication
- [x] Phase 2 – Document Management
- [x] Phase 3 – Cloud Storage (AWS S3)
- [x] Phase 4 – Docker
- [ ] Phase 5 – Deployment
- [ ] Phase 6 – CI/CD
- [ ] Phase 7 – React Frontend