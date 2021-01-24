from src.logics import Logic
from src.managers import manager
from src.schemas import schema


class User(Logic):
    Manager = manager.User
    Schema = schema.User
