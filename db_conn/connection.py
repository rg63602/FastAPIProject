from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config.constants import FASTAPI_MASTERY_DB
from utility.logger.logger import logger

# Create an async engine with connection pooling
async_engine = create_async_engine(
    FASTAPI_MASTERY_DB,
    pool_size=20,
    max_overflow=5,
    future=True,
    echo=False  # Set to True only for debugging
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency function to provide a new async session
async def get_db():
    """Dependency function to get a new async database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database Error: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()
