from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.album_model import Album
from app.schemas.album import AlbumUpdate
from app.actions.album.get_album_action import execute as get_album


def execute(db: Session, album_id: int, data: AlbumUpdate, user_id: int) -> Album:
    album = get_album(db, album_id)
    if album.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this album")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(album, field, value)
    db.commit()
    db.refresh(album)
    return album
