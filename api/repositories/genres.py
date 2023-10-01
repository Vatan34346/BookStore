from fastapi import HTTPException, status
from services import Genre_service


def create(db: Genre_service, data):
    created_genre_id = db.create_genre(data)
    if not created_genre_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'This genra already exists exists')
    return created_genre_id


def genres(db: Genre_service, fields=None, filters=None):
    return db.get_genres(fields=fields, filters=filters)


def show(filed_name, field_value, db: Genre_service):
    genre = db.get_genre(filed_name, field_value)
    if not genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Genre with id: {field_value} not available')

    return genre


def update(id_, updated_data, db: Genre_service):
    genre = db.get_genre('id', id_)

    if not genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Genre with id {id_} not found')

    return db.update_genre(id_, updated_data)


def delete(id_, db: Genre_service):
    genre = db.get_genre('id', id_)
    if not genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Genre with id {id_} not found')
    return db.delete_genre(id_)
