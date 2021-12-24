# project/app/main.py

import os, logging
from fastapi import FastAPI

from app.api.resources import ping, crypto


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(ping.router)
    application.include_router(crypto.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")