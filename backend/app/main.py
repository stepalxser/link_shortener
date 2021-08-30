from fastapi import FastAPI

from link.routers import router as link_router

app = FastAPI()

app.include_router(link_router)