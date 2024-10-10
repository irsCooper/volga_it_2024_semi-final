import asyncio
import asyncpg
import subprocess

async def get_db_ip():
    # Получение IP-адреса Docker-контейнера с PostgreSQL
    result = subprocess.run(["docker", "inspect", "--format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", "doc_postgres"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        ip_address = result.stdout.strip().replace("'", "")
        return ip_address
    else:
        raise Exception(f"Error getting Docker container IP address: {result.stderr}")

async def get_users(db_host):
    # Параметры подключения к базе данных
    db_port = "5432"
    db_name = "semi_final"
    db_user = "postgres"
    db_password = "mypassword"

    # Подключение к базе данных
    conn = await asyncpg.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Выполнение запроса на выборку всех пользователей
    records = await conn.fetch("SELECT * FROM users")

    # Вывод информации о пользователях
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}")

    # Закрытие соединения
    await conn.close()

async def main():
    db_host = await get_db_ip()
    await get_users(db_host)

if __name__ == "__main__":
    asyncio.run(main())
