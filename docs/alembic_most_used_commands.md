# Most Used Alembic Commands
# ==========================

# 1. Initialize Alembic (run once)
alembic init alembic
# → Creates alembic/ folder and alembic.ini configuration

# 2. Generate a new migration script automatically
alembic revision --autogenerate -m "describe changes"
# → Detects changes in models and generates migration file

# 3. Apply all migrations (upgrade to latest)
alembic upgrade head
# → Applies all unapplied migrations

# 4. Roll back last migration (dangerous in production)
alembic downgrade -1
# → Reverts last migration step

# 5. Downgrade to a specific migration revision
alembic downgrade <revision_id>
# → Example: alembic downgrade 1975ea83b712

# 6. Upgrade to a specific migration revision
alembic upgrade <revision_id>
# → Example: alembic upgrade 1975ea83b712

# 7. Show current applied migration version
alembic current
# → Displays the current migration revision in the database

# 8. Show revision history (list of migrations)
alembic history
# → Displays all revision IDs and messages in order

# 9. Stamp the current DB state with a specific revision (without running migration)
alembic stamp head
# → Useful to mark database as up-to-date

# 10. Manually create an empty migration file
alembic revision -m "empty migration"
# → Use when you want to write migration manually

