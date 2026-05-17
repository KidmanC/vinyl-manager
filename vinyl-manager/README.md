# Vinyl Manager

A REST API for managing a music album catalog with user reviews. Built with FastAPI and SQLite.

## Features

- **Album CRUD**: Create, read, update, and delete albums
- **Review system**: Users can review and rate albums (1-5)
- **Authentication**: JWT-based user registration and login
- **Authorization**: Only album/review owners can edit or delete their records
- **Business rule**: Albums with associated reviews cannot be deleted (409 Conflict)
- **Pagination & filtering**: List albums with pagination and genre filter

## Setup

```bash
# Clone and enter the project
cd vinyl-manager

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Run Tests

```bash
pytest -v
```

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/users/register` | No | Register a new user |
| POST | `/users/login` | No | Login, returns JWT token |
| GET | `/albums` | No | List albums (supports `?genre=&page=&page_size=`) |
| GET | `/albums/{id}` | No | Get album details |
| POST | `/albums` | Yes | Create an album |
| PUT | `/albums/{id}` | Yes | Update album (owner only) |
| DELETE | `/albums/{id}` | Yes | Delete album (owner only, no reviews attached) |
| GET | `/albums/{id}/reviews` | No | List reviews for an album |
| POST | `/albums/{id}/reviews` | Yes | Add a review to an album |
| DELETE | `/reviews/{id}` | Yes | Delete a review (owner only) |
| GET | `/health` | No | Health check |

## Project Structure

```
vinyl-manager/
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── database.py        # SQLAlchemy engine and session
│   ├── auth/
│   │   └── jwt.py         # JWT and password utilities
│   ├── models/
│   │   ├── user.py        # User model
│   │   ├── album.py       # Album model
│   │   └── review.py      # Review model
│   ├── schemas/
│   │   ├── user.py        # User Pydantic schemas
│   │   ├── album.py       # Album Pydantic schemas
│   │   └── review.py      # Review Pydantic schemas
│   ├── services/
│   │   ├── user_service.py   # User business logic
│   │   ├── album_service.py  # Album business logic
│   │   └── review_service.py # Review business logic
│   └── routers/
│       ├── users.py       # User endpoints
│       ├── albums.py      # Album endpoints
│       └── reviews.py     # Review endpoints
└── tests/
    ├── conftest.py        # Fixtures (in-memory DB, auth)
    ├── test_users.py      # 4 user tests
    ├── test_albums.py     # 5 album tests
    └── test_reviews.py    # 3 review tests
```
