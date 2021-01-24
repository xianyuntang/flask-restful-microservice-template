from extensions import ma
from src.models import model


class User(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = model.User
