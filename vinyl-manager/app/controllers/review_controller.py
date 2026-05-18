from sqlalchemy.orm import Session

from app.actions.review.create_review_action import execute as create_review_action
from app.actions.review.delete_review_action import execute as delete_review_action
from app.actions.review.read_reviews_action import execute as read_reviews_action
from app.schemas.review import ReviewCreate, ReviewResponse


def read_reviews(db: Session, album_id: int) -> list[ReviewResponse]:
    return read_reviews_action(db, album_id)


def create_review(
    db: Session, album_id: int, data: ReviewCreate, user_id: int
) -> ReviewResponse:
    return create_review_action(db, album_id, data, user_id)


def delete_review(db: Session, review_id: int, user_id: int) -> dict:
    delete_review_action(db, review_id, user_id)
    return {"message": "Review deleted successfully"}
