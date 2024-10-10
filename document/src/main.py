from fastapi import FastAPI, Path
import uvicorn

from .routes import router as router_doctor
 
app = FastAPI(
    title="Doctor Microservices",
)

app.include_router(router_doctor, )
 

