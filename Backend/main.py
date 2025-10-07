from fastapi import FastAPI
from . import models, database
from .routers import auth, users, chats, websocket_manager

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ChatterBox Backend")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(chats.router)
app.include_router(websocket_manager.router)
