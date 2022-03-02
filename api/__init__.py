from fastapi import FastAPI


def register_routers(app: FastAPI):
    from . import (
        screeners,
    )
    app.include_router(screeners.router)