# Cloud Document Management System

A secure cloud-based document management system that enables authenticated users to manage their personal documents through a RESTful API. The application uses PostgreSQL for metadata storage, AWS S3 for file storage, and is containerized with Docker and deployed on Railway.

---

## Live Demo

**API Documentation (Swagger UI)**

https://cloud-document-management-system-production.up.railway.app/docs

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
* Docker
* Railway
* Python 3.12

---

## Features

* Secure JWT authentication
* Upload, download, list, and delete documents
* AWS S3 cloud file storage
* PostgreSQL metadata management
* Dockerized deployment
* Live deployment on Railway

---

## Phase 1: Authentication (Completed)

### Features

* User registration
* User login
* Password hashing
* JWT authentication
* Protected routes

### API Endpoints

* `POST /auth/register`
* `POST /auth/login`
* `GET /users/me`

---

## Phase 2: Document Management (Completed)

### Features

* Upload documents
* List user documents
* Download documents
* Delete documents
* User-based access control

### API Endpoints

* `POST /documents/upload`
* `GET /documents`
* `GET /documents/{document_id}`
* `DELETE /documents/{document_id}`

---

## Phase 3: Cloud Storage (AWS S3) (Completed)

### Features

* AWS S3 integration
* File upload to AWS S3
* File download from AWS S3
* File deletion from AWS S3
* Store file metadata in PostgreSQL

---

## Phase 4: Docker (Completed)

### Features

* Dockerized FastAPI application
* Dockerized PostgreSQL database
* Docker Compose orchestration
* Persistent database volumes
* Health checks
* Environment variable management

---

## Phase 5: Deployment (Completed)

### Features

* Railway deployment
* Cloud PostgreSQL database
* Production environment variables
* Alembic database migrations
* Public API documentation

---

## Future Improvements

* CI/CD with GitHub Actions
* React frontend
* Redis caching
* Background tasks
* Email verification
* Password reset
* Unit & integration testing

---

## Progress

* [x] Phase 1 – Authentication
* [x] Phase 2 – Document Management
* [x] Phase 3 – Cloud Storage (AWS S3)
* [x] Phase 4 – Docker
* [x] Phase 5 – Deployment
* [ ] Phase 6 – CI/CD
* [ ] Phase 7 – React Frontend
