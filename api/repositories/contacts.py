from fastapi import HTTPException, status
from services import Contact_service


def create(db: Contact_service, data):
    created_contact_id = db.create_contact(data)
    if not created_contact_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Contact already exists')
    return created_contact_id


def contacts(db: Contact_service, fields=None, filters=None):
    return db.get_contacts(fields=fields, filters=filters)


def show(filed_name, field_value, db: Contact_service):
    contact = db.get_contact(filed_name, field_value)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Contact with id: {field_value} not available')

    return contact


def update(id_, updated_data, db: Contact_service):
    contact = db.get_contact('id', id_)

    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Contact with id {id_} not found')

    return db.update_contact(id_, updated_data)


def delete(id_, db: Contact_service):
    contact = db.get_contact('id', id_)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Contact with id {id_} not found')
    return db.delete_contact(id_)
