from abc import ABC, abstractmethod


class IUserService(ABC):

    @abstractmethod
    def create_user(self, data):
        pass

    @abstractmethod
    def get_users(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_user(self, _id):
        pass

    @abstractmethod
    def update_user(self, _id, new_data):
        pass

    @abstractmethod
    def get_user(self, field_name, field_value):
        pass
