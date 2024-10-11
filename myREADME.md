# volga_it_2024_semi-final

pip install -r requirements.txt
pip freeze > requirements.txt




docker run -p 5432:5432 --name doc_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:13.3

docker run --name doc_postgres -e POSTGRES_PASSWORD=mypassword -d postgres
docker exec -it doc_postgres psql -U postgres


docker inspect doc_postgres | grep IPAddress



alembic init migrations

хост к бд получать в скрипте
