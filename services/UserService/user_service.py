from .i_user_service import IUserService
from ..BaseSQLServices.base_sql_service import SQLService
from database import TABLE_NAMES


class UserService(IUserService):
    """
    dev: panteleimon gvichia
    description: class that operates with users. Making crud operation on user table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.USER.value
    __sql_service = SQLService()

    @classmethod
    def create_user(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(UserService) create_user: ', e)
            return None

    @classmethod
    def get_users(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(UserService) get_users:', e)
            return None

    @classmethod
    def delete_user(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(UserService) delete_user:', e)
            return False

    @classmethod
    def update_user(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(UserService) update_user:', e)
            return False

    @classmethod
    def get_user(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(UserService) get_user_by_id:', e)
            return False
