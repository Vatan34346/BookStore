from abc import ABC, abstractmethod


class ISQLService(ABC):
    @abstractmethod
    def insert_data(self, table_name, data):
        pass

    @abstractmethod
    def get_data(self, table_name, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_object(self, table_name, _id):
        pass

    @abstractmethod
    def update_object(self, table_name, _id, new_data):
        pass

    @abstractmethod
    def get_object_by_(self, table_name, filed_value, field_value):
        pass
