from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.actions.album.get_album_action import execute as get_album
from app.models.review_model import Review


def execute(db: Session, album_id: int, user_id: int) -> None:
    album = get_album(db, album_id)
    if album.owner_id != user_id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this album"
        )
    review_count = db.query(Review).filter(Review.album_id == album_id).count()
    if review_count > 0:
        raise HTTPException(
            status_code=409,
            detail=(
                "Cannot delete album with associated reviews. Delete the reviews first."
            ),
        )
    db.delete(album)
    db.commit()
