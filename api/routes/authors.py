from fastapi import APIRouter, Depends, status
from typing import List
from ..repositories.authors import authors, delete, update, show, create
from services import Author_Service
from ..schemes import Author, AuthorUpdateCreate
from ..jwt_bearer import JWTBearer

router = APIRouter(
    prefix='/v1/authors',
    tags=['Authors']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Author], dependencies=[Depends(JWTBearer())])
def get_authors(db: Author_Service = Depends(Author_Service)):
    """gets all authors"""
    fields = ['id', 'author_name']
    return authors(db, fields)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def create_author(request: AuthorUpdateCreate, db: Author_Service = Depends(Author_Service)):
    """Creates new author"""
    new_author_data = {
        "author_name": request.author_name,
    }
    id_ = create(db, new_author_data)
    return {
        "created_author_id": id_,
        "status": status.HTTP_201_CREATED
    }


@router.get('/{id_}', status_code=status.HTTP_200_OK, response_model=Author, dependencies=[Depends(JWTBearer())])
def show_author(id_, db:  Author_Service = Depends(Author_Service)):
    """get author by it id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_author(id_, request: AuthorUpdateCreate, db: Author_Service = Depends(Author_Service)):
    """ updates author data"""
    updated_data = {
        "author_name": request.author_name,
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "author successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_author(id_, db: Author_Service = Depends(Author_Service)):
    """ deletes author data"""
    delete(id_, db)
