# project/app/config.py

import os, logging
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    aes_gcm_header: bytes = os.getenv("AES_GCM_HEADER", "NONE")
    aes_key: bytes = os.getenv("AES_KEY", "NONE")
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()