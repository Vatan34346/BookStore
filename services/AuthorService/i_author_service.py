from abc import ABC, abstractmethod


class IAuthorService(ABC):

    @abstractmethod
    def create_author(self, data):
        pass

    @abstractmethod
    def get_authors(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_author(self, _id):
        pass

    @abstractmethod
    def update_author(self, _id, new_data):
        pass

    @abstractmethod
    def get_author(self, field_name, field_value):
        pass
