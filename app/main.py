from http import HTTPStatus
from fastapi import FastAPI

app = FastAPI(title="Globant Data",
    description="Globant Data",
    version="1.0.0",)

app.include_router(view_jimmy.router)