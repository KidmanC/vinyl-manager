from fastapi import FastAPI

from app.core.database import engine, Base
from app.routes import user_routes, album_routes, review_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vinyl Manager", version="1.0.0")

app.include_router(user_routes.router)
app.include_router(album_routes.router)
app.include_router(review_routes.router)


@app.get("/health")
def health():
    return {"status": "ok"}
