from abc import ABC, abstractmethod


class IConditionService(ABC):

    @abstractmethod
    def create_condition(self, data):
        pass

    @abstractmethod
    def get_conditions(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_condition(self, _id):
        pass

    @abstractmethod
    def update_condition(self, _id, new_data):
        pass

    @abstractmethod
    def get_condition(self, field_name, field_value):
        pass
