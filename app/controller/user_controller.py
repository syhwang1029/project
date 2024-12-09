#user_router
from model import user
from mongodb.mongodb import user_collection


async def crate_user(self, name, email, password):
    user = dict(
        name = name,
        email = email,
        password = password
    )
    await user_collection
    