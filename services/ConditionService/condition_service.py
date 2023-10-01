from .i_condition_service import IConditionService
from database import TABLE_NAMES
from ..BaseSQLServices.base_sql_service import SQLService


class ConditionService(IConditionService):
    """
    dev: panteleimon gvichia
    description: class that operates with Conditions. Making crud operation on Conditions table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.CONDITIONS.value
    __sql_service = SQLService()

    @classmethod
    def create_condition(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(ConditionService) create_condition: ', e)
            return None

    @classmethod
    def get_conditions(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(ConditionService) get_conditions:', e)
            return None

    @classmethod
    def delete_condition(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(ConditionService) delete_condition:', e)
            return False

    @classmethod
    def update_condition(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(ConditionService) update_condition:', e)
            return False

    @classmethod
    def get_condition(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(ConditionService) get_condition:', e)
            return False
