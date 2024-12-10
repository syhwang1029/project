#user_router
from model import user

async def crate_user(self, name, email, password):
    user = dict(
        name = name,
        email = email,
        password = password
    )
    