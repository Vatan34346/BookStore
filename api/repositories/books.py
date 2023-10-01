from fastapi import HTTPException, status
from services import Book_service, User_Service


def create(db: Book_service, data):
    created_book_id = db.create_book(data)
    if not created_book_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Book already exists')
    return created_book_id


def books(db: Book_service, fields=None, filters=None):
    return db.get_books(fields=fields, filters=filters)


def show(filed_name, field_value, db: Book_service):
    book = db.get_book(filed_name, field_value)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id: {field_value} not available')

    return book


def update(id_, updated_data, db: Book_service):
    book = db.get_book('id', id_)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {id_} not found')

    return db.update_book(id_, updated_data)


def delete(id_, db: Book_service):
    book = db.get_book('id', id_)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {id_} not found')
    return db.delete_book(id_)


def interested_in_book(user_id, book_id, db: Book_service, user_service: User_Service):
    book = db.get_book('id', book_id)
    user = user_service.get_user('id', user_id)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {book_id} not found')

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} not found')

    interested_users = book['listOfInterestedUsers'] + ', ' + str(user_id)

    updated_data = {
        "listOfInterestedUsers": interested_users
    }

    return db.update_book(book_id, updated_data)



