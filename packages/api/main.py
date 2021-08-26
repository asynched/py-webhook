from fastapi import FastAPI
from packages.api.config import configure_app
from packages.api.routes.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

configure_app(app)
