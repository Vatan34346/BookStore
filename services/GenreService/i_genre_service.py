from abc import ABC, abstractmethod


class IGenreService(ABC):

    @abstractmethod
    def create_genre(self, data):
        pass

    @abstractmethod
    def get_genres(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_genre(self, _id):
        pass

    @abstractmethod
    def update_genre(self, _id, new_data):
        pass

    @abstractmethod
    def get_genre(self, field_name, field_value):
        pass
