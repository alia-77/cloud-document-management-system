# Cloud Document Management System

A backend API for a cloud-based document management system built with **FastAPI** and **PostgreSQL**.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Passlib (bcrypt)
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

## Phase 2 (Next)

* Create Document model
* Upload files
* Store file metadata
* Associate documents with users
* List user documents
* Download documents
* Delete documents
* Restrict users to their own files

---

## Future Improvements

* AWS S3 storage
* Docker
* Redis caching
* Background tasks
* Email verification
* Password reset
* CI/CD
* Deployment
* Unit and integration tests

---

## Progress

* [x] Phase 1 – Authentication
* [ ] Phase 2 – Document Management
* [ ] Phase 3 – Cloud Storage (AWS S3)
* [ ] Phase 4 – Docker
* [ ] Phase 5 – Deployment
* [ ] Phase 6 – CI/CD
