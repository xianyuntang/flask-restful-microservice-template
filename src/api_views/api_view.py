from src.api_views import ApiView
from src.logics import logic


class User(ApiView):
    Logic = logic.User
