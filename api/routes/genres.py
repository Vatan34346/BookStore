from fastapi import APIRouter, Depends, status
from typing import List
from ..repositories.genres import genres, delete, update, show, create
from services import Genre_service
from ..schemes import Genre, GenreUpdateCreate
from ..jwt_bearer import JWTBearer

router = APIRouter(
    prefix='/v1/genres',
    tags=['Genres']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Genre], dependencies=[Depends(JWTBearer())])
def get_genres(db: Genre_service = Depends(Genre_service)):
    """gets all genres"""
    fields = ['id', 'genre_name']
    return genres(db, fields)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def create_genre(request: GenreUpdateCreate, db: Genre_service = Depends(Genre_service)):
    """Creates new genre"""
    new_genre_data = {
        "genre_name": request.genre_name,
    }
    id_ = create(db, new_genre_data)
    return {
        "created_genre_id": id_,
        "status": status.HTTP_201_CREATED
    }


@router.get('/{id_}', status_code=status.HTTP_200_OK, response_model=Genre, dependencies=[Depends(JWTBearer())])
def show_genre(id_, db:  Genre_service = Depends(Genre_service)):
    """get genre by it id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_genre(id_, request: GenreUpdateCreate, db: Genre_service = Depends(Genre_service)):
    """ updates genre data"""
    updated_data = {
        "genre_name": request.genre_name,
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "genre successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_genre(id_, db: Genre_service = Depends(Genre_service)):
    """ deletes genre data"""
    delete(id_, db)
