from src.database.models import UserDB
from src.models.user import UserLogin
from src.prototypes.user_repo_prototype import UserRepoPrototype


class UserRepository(UserRepoPrototype):
    def __init__(self) -> None:
        pass

    async def create_user(self, user: UserDB) -> UserDB:
        pass

    async def update_user(self, user: UserDB, user_id: int) -> UserDB:
        pass

    async def get_user(self, user_login: UserLogin) -> UserDB:
        pass

    async def delete_user(self, user_login: UserLogin) -> UserDB:
        pass
