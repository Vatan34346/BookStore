from fastapi import HTTPException, status
from services import User_Service, Book_service


def users(db: User_Service, fields=None, filters=None):
    return db.get_users(fields=fields, filters=filters)


def show(filed_name, field_value, db: User_Service):
    user = db.get_user(filed_name, field_value)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {field_value} not available')

    return user


def update(id_, updated_data, db: User_Service):
    user = db.get_user('id', id_)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id_} not found')

    return db.update_user(id_, updated_data)


def delete(id_, db: User_Service):
    user = db.get_user('id', id_)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id_} not found')
    return db.delete_user(id_)


def sell(new_owner_id, book_id, db: User_Service, book_service: Book_service):
    book = book_service.get_book('id', book_id)
    new_owner = db.get_user('id', new_owner_id)



    if not new_owner:
        print('hi no yser')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {new_owner} not found')

    if not book:
        print('hi no book')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {book_id} not found')

    updated_data = {
        "users_id": new_owner_id,
        "listOfInterestedUsers": ''
    }

    return book_service.update_book(book_id, updated_data)



