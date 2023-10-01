from fastapi import HTTPException, status
from services import Condition_Service


def create(db: Condition_Service, data):
    created_condition_id = db.create_condition(data)
    if not created_condition_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Condition already exists')
    return created_condition_id


def conditions(db: Condition_Service, fields=None, filters=None):
    return db.get_conditions(fields=fields, filters=filters)


def show(filed_name, field_value, db: Condition_Service):
    condition = db.get_condition(filed_name, field_value)
    if not condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Condition with id: {field_value} not available')

    return condition


def update(id_, updated_data, db: Condition_Service):
    condition = db.get_condition('id', id_)

    if not condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Condition with id {id_} not found')

    return db.update_condition(id_, updated_data)


def delete(id_, db: Condition_Service):
    condition = db.get_condition('id', id_)
    if not condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Condition with id {id_} not found')
    return db.delete_condition(id_)
