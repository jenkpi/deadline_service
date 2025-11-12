import asyncio
import logging
from app.core.bootstrap import get_task_deadline_service
from app.main import app


logger = logging.getLogger("faststream")


@app.after_startup
async def after_startup_hook():
    logger.info("after_startup called")
    asyncio.create_task(get_task_deadline_service().deadline_manager())
