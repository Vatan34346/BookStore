from .i_author_service import IAuthorService
from database import TABLE_NAMES
from ..BaseSQLServices.base_sql_service import SQLService


class AuthorService(IAuthorService):
    """
    dev: panteleimon gvichia
    description: class that operates with Authors. Making crud operation on Authors table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.AUTHORS.value
    __sql_service = SQLService()

    @classmethod
    def create_author(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(AuthorService) create_author: ', e)
            return None

    @classmethod
    def get_authors(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(AuthorService) get_author:', e)
            return None

    @classmethod
    def delete_author(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(AuthorService) delete_author:', e)
            return False

    @classmethod
    def update_author(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(AuthorService) update_author:', e)
            return False

    @classmethod
    def get_author(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(AuthorService) get_author:', e)
            return False
