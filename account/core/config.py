from pathlib import Path
from os import getenv, path

from pydantic_settings import BaseSettings
from pydantic import BaseModel, SecretStr

import docker

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_echo: bool = True
    container_name:str

    class Config:
        env_file = path.expanduser(f'{BASE_DIR}/.env')

    def db_url(container_name):
        # Создаем клиент Docker
        client = docker.from_env()
        
        try:
            container = client.containers.get(container_name)
            host = container.attrs['NetworkSettings']['Networks']['bridge']['IPAddress']

            return f"postgresql://postgres:postgres@{host}:5432/account"
            
        except docker.errors.NotFound:
            print(f"Container '{container_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
settings = Settings()



class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "cert" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "cert" / "jwt-public.pem"


