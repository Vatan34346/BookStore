from fastapi import FastAPI
from .routes.authentification import router as auth_router
from .routes.user import router as user_router
from .routes.authors import router as author_router
from .routes.genres import router as genre_router
from .routes.conditions import router as condition_router
from .routes.contacts import router as contact_router
from .routes.books import router as book_router


def create_app():
    app = FastAPI()

    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(author_router)
    app.include_router(genre_router)
    app.include_router(condition_router)
    app.include_router(contact_router)
    app.include_router(book_router)

    return app
