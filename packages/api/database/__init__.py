from peewee import SqliteDatabase, Model

database = SqliteDatabase("api.sqlite3")


class BaseModel(Model):
    class Meta:
        database = database
