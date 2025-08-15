# 📝 Blog App – FastAPI + Vue + MySQL

A modern, secure, and scalable blog application built with **FastAPI** (backend), **Vue.js** (frontend), and **MySQL** (database).  
Designed with **API-first architecture**, **JWT-based authentication**, and **role-based access control** to ensure flexibility and security.

---

## 🚀 Features

### Backend (FastAPI)
- **Fast, async REST API** with automatic docs (Swagger & ReDoc)
- **OAuth2 Authorization Code Flow with PKCE** for secure login
- **JWT access tokens** with short expiration
- **Refresh token rotation** with revocation
- **OTP email login** (powered by Brevo)
- **Role-based access control** (Admin / User)
- **Alembic migrations** for database schema changes
- **Pydantic models** for request/response validation

### Frontend (Vue.js)
- Modern, responsive UI
- Admin dashboard for post & category management
- Markdown editor for creating rich blog posts
- Multilingual support (planned)
- Token-based authentication flow

### Database (MySQL)
- **Normalized schema** for posts, categories, users, and OTP codes
- **Slug generation** for SEO-friendly URLs
- Optimized queries with SQLAlchemy ORM
