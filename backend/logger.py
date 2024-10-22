from loguru import logger
import sys
from .config import settings

logger.remove()
logger.add(sys.stderr, level=settings.LOG_LEVEL, serialize=True)
