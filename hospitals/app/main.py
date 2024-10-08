from fastapi import FastAPI, Path
import uvicorn

from app.routes import router as router_doctor
 
app = FastAPI(
    title="Doctor Microservices",
)

app.include_router(router_doctor, )
 

