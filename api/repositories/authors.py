from fastapi import HTTPException, status
from services import Author_Service


def create(db: Author_Service, data):
    created_author_id = db.create_author(data)
    if not created_author_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Author already exists')
    return created_author_id


def authors(db: Author_Service, fields=None, filters=None):
    return db.get_authors(fields=fields, filters=filters)


def show(filed_name, field_value, db: Author_Service):
    author = db.get_author(filed_name, field_value)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Author with id: {field_value} not available')

    return author


def update(id_, updated_data, db: Author_Service):
    author = db.get_author('id', id_)

    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Author with id {id_} not found')

    return db.update_author(id_, updated_data)


def delete(id_, db: Author_Service):
    author = db.get_author('id', id_)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Author with id {id_} not found')
    return db.delete_author(id_)
