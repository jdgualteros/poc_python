import uvicorn
from fastapi import FastAPI
from app.views import v_uploads

app = FastAPI(title="Globant Data",
    description="Globant Data",
    version="1.0.0",)

app.include_router(v_uploads.router)
