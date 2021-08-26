from peewee import CharField
from packages.api.database import BaseModel


class User(BaseModel):
    name = CharField(max_length=64)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
