from fastapi import APIRouter, Depends, status
from typing import List
from ..repositories.conditions import conditions, delete, update, show, create
from services import Condition_Service
from ..schemes import Condition, ConditionUpdateCreate
from ..jwt_bearer import JWTBearer

router = APIRouter(
    prefix='/v1/conditions',
    tags=['Conditions']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Condition], dependencies=[Depends(JWTBearer())])
def get_conditions(db: Condition_Service = Depends(Condition_Service)):
    """gets all conditions"""
    fields = ['id', 'condition_name']
    return conditions(db, fields)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def create_condition(request: ConditionUpdateCreate, db: Condition_Service = Depends(Condition_Service)):
    """Creates new condition"""
    new_condition_data = {
        "condition_name": request.condition_name,
    }
    id_ = create(db, new_condition_data)
    return {
        "created_condition_id": id_,
        "status": status.HTTP_201_CREATED
    }


@router.get('/{id_}', status_code=status.HTTP_200_OK, response_model=Condition, dependencies=[Depends(JWTBearer())])
def show_condition(id_, db:  Condition_Service = Depends(Condition_Service)):
    """get condition by it id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_condition(id_, request: ConditionUpdateCreate, db: Condition_Service = Depends(Condition_Service)):
    """ updates condition data"""
    updated_data = {
        "condition_name": request.condition_name,
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "condition successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_condition(id_, db: Condition_Service = Depends(Condition_Service)):
    """ deletes author data"""
    delete(id_, db)
