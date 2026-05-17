from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.album_model import Album


def execute(db: Session, album_id: int) -> Album:
    album = db.query(Album).filter(Album.id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album
