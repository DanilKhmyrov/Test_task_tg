import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routers import main_router
from app.core import logger
from app.core.utils import update_transaction_statuses
from app.core.db import AsyncSessionLocal



@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info('Starting background task for updating transaction statuses.')
        async with AsyncSessionLocal() as session:
            task = asyncio.create_task(update_transaction_statuses(session))
            yield

    except Exception as e:
        logger.error(f'Error during lifespan execution: {e}')
    finally:
        task.cancel()
        logger.info('Background task cancelled.')

app = FastAPI(lifespan=lifespan)

app.include_router(main_router)
