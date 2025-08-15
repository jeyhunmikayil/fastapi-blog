# Alembic Setup Guide for Blog API

This guide will help you set up Alembic for managing your database migrations in the Blog API project using FastAPI + SQLAlchemy + MySQL.

---

## 1. Install Alembic

Activate your virtual environment and run:

    pip install alembic

---

## 2. Initialize Alembic

In the project root (same level as `app/`):

    alembic init alembic

This will create:

    /alembic/
    alembic.ini

---

## 3. Configure Alembic

### a. Update `alembic.ini`

Find the line:

    sqlalchemy.url = driver://user:pass@localhost/dbname

Update it with your actual connection string:

    sqlalchemy.url = mysql+pymysql://user:password@localhost/blogdb

Or, to load from `.env` dynamically (advanced), leave it unchanged and configure via `env.py`.

---

### b. Modify `alembic/env.py`

Import your Base and models at the top:

    from app.core.database import Base
    from app import models  # ensure __init__.py in app/models imports all models

Update metadata configuration:

    target_metadata = Base.metadata

This tells Alembic to track models defined in your application.

---

## 4. Create Migration Script

To autogenerate migration based on models:

    alembic revision --autogenerate -m "Initial migration"

Alembic will generate a file in `alembic/versions/`.

Review it and ensure it reflects your intended schema.

---

## 5. Apply the Migration

Run:

    alembic upgrade head

This applies the migration and creates tables in your database.

---

## Notes

- Always commit migration files to version control.
- To generate new migrations after model changes:

      alembic revision --autogenerate -m "Describe the change"

- Apply them again with:

      alembic upgrade head

---

For more info, visit: https://alembic.sqlalchemy.org/

