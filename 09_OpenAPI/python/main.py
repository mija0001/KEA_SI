from fastapi import FastAPI

app = FastAPI()

from routers import spacecraft_router
from routers import datetime_router
app.include_router(spacecraft_router)
app.include_router(datetime_router)