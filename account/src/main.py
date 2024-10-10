from fastapi import FastAPI

from src.routes_authentication import router as router_authentication
from src.routes_accounts import router as router_accounts
from src.routes_doctor import router as router_doctor

import uvicorn

app = FastAPI(
    title="Account Microservices",
)

app.include_router(router_authentication)
app.include_router(router_accounts)
app.include_router(router_doctor)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)