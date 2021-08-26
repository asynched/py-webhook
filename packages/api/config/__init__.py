from fastapi import FastAPI
from packages.api.database import database
from packages.api.models.user import User


def configure_app(app: FastAPI):
    database.create_tables(
        [
            User,
        ]
    )
