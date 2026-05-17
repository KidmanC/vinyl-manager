from sqlalchemy.orm import Session

from app.schemas.album import AlbumCreate, AlbumUpdate, AlbumResponse, AlbumListResponse
from app.actions.album.list_albums_action import execute as list_albums
from app.actions.album.get_album_action import execute as get_album
from app.actions.album.create_album_action import execute as create_album
from app.actions.album.update_album_action import execute as update_album
from app.actions.album.delete_album_action import execute as delete_album


def list_endpoint(
    db: Session, page: int, page_size: int, genre: str | None
) -> AlbumListResponse:
    items, total = list_albums(db, page, page_size, genre)
    return AlbumListResponse(items=items, total=total, page=page, page_size=page_size)


def get_endpoint(db: Session, album_id: int) -> AlbumResponse:
    return get_album(db, album_id)


def create_endpoint(db: Session, data: AlbumCreate, owner_id: int) -> AlbumResponse:
    return create_album(db, data, owner_id)


def update_endpoint(
    db: Session, album_id: int, data: AlbumUpdate, user_id: int
) -> AlbumResponse:
    return update_album(db, album_id, data, user_id)


def delete_endpoint(db: Session, album_id: int, user_id: int) -> None:
    delete_album(db, album_id, user_id)
