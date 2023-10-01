from .i_genre_service import IGenreService
from database import TABLE_NAMES
from ..BaseSQLServices.base_sql_service import SQLService


class GenreService(IGenreService):
    """
    dev: panteleimon gvichia
    description: class that operates with genres. Making crud operation on genres table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.GENRES.value
    __sql_service = SQLService()

    @classmethod
    def create_genre(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(GenreService) create_genre: ', e)
            return None

    @classmethod
    def get_genres(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(GenreService) get_genres:', e)
            return None

    @classmethod
    def delete_genre(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(GenreService) delete_genre:', e)
            return False

    @classmethod
    def update_genre(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(GenreService) update_genre:', e)
            return False

    @classmethod
    def get_genre(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(GenreService) get_genre:', e)
            return False
