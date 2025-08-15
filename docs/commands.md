uvicorn app.main:app --port=8090 --reload
source venv/bin/activate

zip -r project.zip . -x "*/__pycache__/*" "*.pyc" "venv/*"


uvicorn app.main:app --host=127.0.0.1 --port=8093 --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

http://127.0.0.1:8093/docs


firewall settings Custom	8095	ipv4	0.0.0.0/0	Fastapi test
find . | sort

alembic init alembic
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head
