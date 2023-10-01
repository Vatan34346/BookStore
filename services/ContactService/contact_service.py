from .i_contact_service import IContactService
from database import TABLE_NAMES
from ..BaseSQLServices.base_sql_service import SQLService


class ContactService(IContactService):
    """
    dev: panteleimon gvichia
    description: class that operates with contacts. Making crud operation on contacts table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.CONTACTS.value
    __sql_service = SQLService()

    @classmethod
    def create_contact(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(ContactService) create_contact: ', e)
            return None

    @classmethod
    def get_contacts(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(ContactService) get_contacts:', e)
            return None

    @classmethod
    def delete_contact(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(ContactService) delete_contact:', e)
            return False

    @classmethod
    def update_contact(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(ContactService) update_contact:', e)
            return False

    @classmethod
    def get_contact(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(ContactService) get_contact:', e)
            return False
