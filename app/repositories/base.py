from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository(ABC):
    @abstractmethod
    async def add(self, entity, db: AsyncSession): pass

    @abstractmethod
    async def get(self, id: int, db: AsyncSession): pass

    @abstractmethod
    async def list(self, db: AsyncSession): pass