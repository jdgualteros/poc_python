import uvicorn
from fastapi import FastAPI
from app.views import v_uploads, requirements, backups
from starlette.responses import RedirectResponse

app = FastAPI(title="Globant Data",
    description="Globant Data",
    version="1.0.0",)

app.include_router(v_uploads.router)
app.include_router(requirements.router)
app.include_router(backups.router)

@app.get("/")
def main():
   return RedirectResponse(url="/docs/")