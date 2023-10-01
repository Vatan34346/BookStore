from abc import ABC, abstractmethod


class IBookService(ABC):

    @abstractmethod
    def create_book(self, data):
        pass

    @abstractmethod
    def get_books(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_book(self, _id):
        pass

    @abstractmethod
    def update_book(self, _id, new_data):
        pass

    @abstractmethod
    def get_book(self, field_name, field_value):
        pass
