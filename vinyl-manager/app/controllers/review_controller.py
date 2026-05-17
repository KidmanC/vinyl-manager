from sqlalchemy.orm import Session

from app.actions.review.create_review_action import execute as create_review
from app.actions.review.delete_review_action import execute as delete_review
from app.actions.review.list_reviews_action import execute as list_reviews
from app.schemas.review import ReviewCreate, ReviewResponse


def list_endpoint(db: Session, album_id: int) -> list[ReviewResponse]:
    return list_reviews(db, album_id)


def create_endpoint(
    db: Session, album_id: int, data: ReviewCreate, user_id: int
) -> ReviewResponse:
    return create_review(db, album_id, data, user_id)


def delete_endpoint(db: Session, review_id: int, user_id: int) -> None:
    delete_review(db, review_id, user_id)
