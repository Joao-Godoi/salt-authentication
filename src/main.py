from fastapi import FastAPI

from .core.database import Base, engine
from .routes.user_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix="/users")
