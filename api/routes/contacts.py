from fastapi import APIRouter, Depends, status
from typing import List
from ..repositories.contacts import contacts, delete, update, show, create
from services import Contact_service
from ..schemes import Contact, ContactUpdateCreate
from ..jwt_bearer import JWTBearer

router = APIRouter(
    prefix='/v1/contacts',
    tags=['Contacts']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Contact], dependencies=[Depends(JWTBearer())])
def get_contacts(db: Contact_service = Depends(Contact_service)):
    """gets all contacts"""
    fields = ['id', 'address', 'phone', 'coordinates']
    return contacts(db, fields)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def create_contact(request: ContactUpdateCreate, db: Contact_service = Depends(Contact_service)):
    """Creates new author"""
    new_contact_data = {
        "address": request.address,
        "phone": request.phone,
        "coordinates": f'long: {request.coordinates.log} lat: {request.coordinates.lat}'
    }
    id_ = create(db, new_contact_data)
    return {
        "created_contact_id": id_,
        "status": status.HTTP_201_CREATED
    }


@router.get('/{id_}', status_code=status.HTTP_200_OK, response_model=Contact, dependencies=[Depends(JWTBearer())])
def show_contact(id_, db:  Contact_service = Depends(Contact_service)):
    """get contact by it id for displaying"""
    field_name = 'id'
    return show(field_name, id_, db)


@router.put('/{id_}/update', status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_contact(id_, request: ContactUpdateCreate, db: Contact_service = Depends(Contact_service)):
    """ updates contact data"""
    updated_data = {
        "address": request.address,
        "phone": request.phone,
        "coordinates": f'long: {request.coordinates.log} lat: {request.coordinates.lat}'
    }
    return {
        "is_updated": update(id_, updated_data, db),
        "msg": "contact successfully updated"
    }


@router.delete('/{id_}/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def delete_contact(id_, db: Contact_service = Depends(Contact_service)):
    """ deletes contact data"""
    delete(id_, db)
