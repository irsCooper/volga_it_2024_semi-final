
from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent



class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "cert" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "cert" / "jwt-public.pem"

# class Settings(BaseModel):
