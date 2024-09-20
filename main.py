from typing import Optional, Annotated

from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base is clear")
    await create_tables()
    print("Base is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)



tasks = []



