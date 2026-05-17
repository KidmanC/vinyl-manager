# Agentic Process Documentation

## Tools Used

- **Opencode (big-pickle model)** — AI coding assistant used throughout development. All code was written collaboratively through conversation.

## My Approach

I structured the work in iterative layers rather than generating everything at once:

1. **Planned the architecture** — Discussed project domain, chose Vinyl Manager (music album catalog with reviews), and agreed on a layered architecture: routes → controllers → actions → models → DB.

2. **Built layer by layer** — Each layer was implemented and verified before moving to the next:
   - Core (database, config, security)
   - ORM models
   - Pydantic schemas
   - Business logic actions
   - Controllers
   - Routes
   - Tests

3. **Applied a skill** — Installed the official `fastapi/fastapi` skill mid-project to align with FastAPI best practices (Annotated pattern, router conventions).

4. **Refactored architecture** — Changed from a services/repositories structure to the current routes/controllers/actions pattern based on my preference.

5. **Incremental commits** — Made one commit per layer so the history tells the build story.

## Key Prompts

### Prompt 1: Initial project structure
> "Opción 2: Gestor de Listas Musicales (Vinyl Manager) ... CRUD: similar ... Regla de negocio: un álbum no se puede eliminar si tiene reseñas asociadas"

The AI generated the initial project structure with FastAPI + SQLite, including models, schemas, services, and routers. I accepted it because it matched the requirements, but later refactored the architecture.

### Prompt 2: Architecture refactoring
> "no veo los controladores por ejemplo. no estas usando clean architecture"

I asked the AI to restructure from a flat services/repositories pattern to a cleaner routes → controllers → actions → models architecture. The AI created separate action files (one per use case), controller files for orchestration, and route files for HTTP definitions.

### Prompt 3: Apply FastAPI skill
> "la primera" (installing fastapi/fastapi skill)

After installing the official FastAPI skill, the AI updated the code to use the `Annotated` pattern for dependencies (`SessionDep`, `CurrentUser` type aliases) and aligned router conventions. I accepted this as it follows official best practices.

## Critical Evaluation

### Piece of code: Album deletion with business rule (`delete_album_action.py`)

**What the AI got right:**
- Correctly implemented the business rule: albums with reviews return 409 Conflict
- Properly extracted get_album as a reusable action
- Separated authorization (owner check) from the business rule

**What I improved:**
- The AI originally put the business logic in a service class. I asked for it to be split into individual action files, each with a single `execute()` function, matching my preferred architecture from backend classes.
- Added explicit HTTP status codes (403, 404, 409) aligned with REST standards.

**Verification:**
- The test `test_delete_album_with_reviews_blocked` directly validates this rule by creating an album, adding a review, then attempting deletion and asserting 409.
- All 12 tests pass with `pytest -v`.

**Security considerations:**
- JWT tokens use `str(user.id)` as sub claim (required by python-jose)
- Password hashing via bcrypt (passlib)
- The SECRET_KEY has a fallback for development but is configurable via environment variable
- No hardcoded credentials or secrets in the codebase

## What I Learned

- **Python module naming constraints:** Files with dots (e.g., `user.model.py`) cannot be imported using standard Python import syntax. Used underscores (`user_model.py`) instead while keeping the conceptual structure.
- **FastAPI `Annotated` pattern:** The official FastAPI skill recommends `Annotated[Session, Depends(get_db)]` over the traditional `db: Session = Depends(get_db)` syntax. This keeps function signatures cleaner and type annotations working.
- **JWT sub claim type:** python-jose strictly requires the `sub` claim to be a string, not an integer, or it raises `JWTClaimsError`.
- **Clean Architecture in FastAPI:** There are multiple valid approaches (services vs. actions, repositories vs. direct queries). The right choice depends on team preference and project scale.
