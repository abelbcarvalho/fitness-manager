from abc import ABC, abstractmethod

from src.database.models import UserDB
from src.models.user import UserLogin


class UserRepoPrototype(ABC):
    @abstractmethod
    async def create_user(self, user: UserDB) -> UserDB:
        pass

    @abstractmethod
    async def get_user(self, user_login: UserLogin) -> UserDB:
        pass

    @abstractmethod
    async def update_user(self, user: UserDB, user_id: int) -> UserDB:
        pass

    @abstractmethod
    async def delete_user(self, user_login: UserLogin) -> bool:
        pass
