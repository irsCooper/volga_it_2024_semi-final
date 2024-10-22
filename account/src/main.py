from contextlib import asynccontextmanager
from fastapi import FastAPI

from account.src.routes.routes_authentication import router as router_authentication
from account.src.routes.routes_accounts import router as router_accounts
from account.src.routes.routes_doctor import router as router_doctor

from account.src.models.base import Base
from account.src.models.db_helper import db_helper

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield





app = FastAPI(
    title="Account Microservices",
    lifespan=lifespan
)

app.include_router(router_authentication)
app.include_router(router_accounts)
app.include_router(router_doctor)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)