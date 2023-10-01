from fastapi import APIRouter, Depends, status
from ..repositories.books import books, delete, update, show, create, interested_in_book
from services import Book_service, User_Service
from ..schemes import BookUpdateCreate
from ..jwt_bearer import JWTBearer

router = APIRouter(
    prefix='/v1/books',
    tags=['Books']
)


@router.get('/', status_code=status.HTTP_200_OK)
def get_books(authors_id: int = None,  genres_id: int = None, conditions_id: int = None, contacts_id: int = None, users_id: int = None, db: Book_service = Depends(Book_service)):
    """gets all books filtered, by default all filter params are None so method will retrieve all books.
    You can aplay filtering params by /books/?genres_id=5&conditions_id=20 in url or use needed input in swagger in method's Parameters section
    """
    filter_data = {
        "authors_id": authors_id if isinstance(authors_id, int) else None,
        "genres_id": genres_id if isinstance(genres_id, int) else None,
        "conditions_id": conditions_id if isinstance(conditions_id, int) else None,
        "contacts_id": contacts_id if isinstance(contacts_id, int) else None,
        "users_id": users_id if isinstance(users_id, int) else None
    }
    filters = {key: value for key, value in filter_data.items() if value is not None}
    if len(filters) == 0:
        filters = None

    fields = ['id', 'book_title', "book_description", "authors_id",  "genres_id", "conditions_id", "contacts_id", "users_id", "listOfInterestedUsers"]

    return books(db, fields, filters=filters)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def create_book(request: BookUpdateCreate, db: Book_service = Depends(Book_service)):
    """Creates new book"""
    new_book_data = {
        "book_title": request.book_title,
        "book_description": request.book_description,
        "authors_id": request.authors_id,
        "genres_id": request.genres_id,
        "conditions_id": request.conditions_id,
        "contacts_id": request.contacts_id,
        "users_id": request.users_id,
        "listOfInterestedUsers": request.listOfInterestedUsers
    }
    id_ = create(db, new_book_data)
    return {
        "created_author_id": id_,
        "status": status.HTTP_201_CREATED
    }


@router.get('/{id_}', status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def show_book(id_, db:  Book_service = Depends(Book_service)):
    """get book by it id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_book(id_, request: BookUpdateCreate, db: Book_service = Depends(Book_service)):
    """ updates book data"""
    updated_data = {
        "book_title": request.book_title,
        "book_description": request.book_description,
        "authors_id": request.authors_id,
        "genres_id": request.genres_id,
        "conditions_id": request.conditions_id,
        "contacts_id": request.contacts_id,
        "users_id": request.users_id,
        "listOfInterestedUsers": request.listOfInterestedUsers
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "book successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_book(id_, db: Book_service = Depends(Book_service)):
    """ deletes book data"""
    delete(id_, db)


@router.put('/{id_}/interested_user/{user_id}', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def choose_book_to_purchase(id_: int, user_id: int, db: Book_service = Depends(Book_service), user_service: User_Service = Depends(User_Service)):
    """this route is for method saves user's id how wants to buy book in book's listOfInterestedUsers field. So then we can retrieve this list.
    split it by "," and convert to int in purpose of usage on front.
    """
    is_interested = interested_in_book(user_id, id_, db, user_service)
    return {
        "is_interested": is_interested,
        "msg": "We will send to book owner info about you. And he will contact you as soon as possible."
    }
