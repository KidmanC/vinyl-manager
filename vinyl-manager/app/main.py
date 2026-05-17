from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.database import Base, engine
from app.routes import album_routes, review_routes, user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vinyl Manager", version="1.0.0")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()},
    )

app.include_router(user_routes.router)
app.include_router(album_routes.router)
app.include_router(review_routes.router)


@app.get("/health")
def health():
    return {"status": "ok"}
