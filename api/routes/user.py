from fastapi import APIRouter, Depends, status
from typing import List
from ..repositories.user import users, delete, update, show, sell
from services import User_Service, Book_service
from ..schemes import User, UserUpdate
from ..jwt_bearer import JWTBearer
from helpers import hash_

router = APIRouter(
    prefix='/v1/users',
    tags=['Users']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[User], dependencies=[Depends(JWTBearer())])
def get_users(db: User_Service = Depends(User_Service)):
    """gets all users"""
    fields = ['id', 'name', 'email']
    return users(db, fields)


@router.get('/{id_}', status_code=status.HTTP_200_OK, response_model=User, dependencies=[Depends(JWTBearer())])
def show_user(id_, db:  User_Service = Depends(User_Service)):
    """get user by its id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_user(id_, request: UserUpdate, db: User_Service = Depends(User_Service)):
    """ updates user data"""
    updated_data = {
        "name": request.name,
        "email": request.email,
        "password": hash_.bcrypt(request.password)
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "User successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_user(id_, db: User_Service = Depends(User_Service)):
    """ deletes user data"""
    delete(id_, db)


@router.put('/{book_id}/sold/{new_owner_id}', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def sell_book(book_id: int, new_owner_id: int, db: User_Service = Depends(User_Service), book_service: Book_service = Depends(Book_service)):
    """this route is for choosing new owner of your book."""
    is_sold = sell(new_owner_id, book_id, db, book_service)
    return {
        "is_sold": is_sold,
        "msg": f"Your book is sold to new owner with id: {new_owner_id}"
    }
