from .i_book_service import IBookService
from database import TABLE_NAMES
from ..BaseSQLServices.base_sql_service import SQLService


class BookService(IBookService):
    """
    dev: panteleimon gvichia
    description: class that operates with Books. Making crud operation on Books table.
    phone: +7995123456
    """
    __table_name = TABLE_NAMES.BOOKS.value
    __sql_service = SQLService()

    @classmethod
    def create_book(cls, data):
        try:
            return cls.__sql_service.insert_data(cls.__table_name, data)

        except Exception as e:
            print('Error(BookService) create_book: ', e)
            return None

    @classmethod
    def get_books(cls, fields=None, filters=None):
        try:
            return cls.__sql_service.get_data(cls.__table_name, fields, filters)
        except Exception as e:
            print('Error(BookService) get_books:', e)
            return None

    @classmethod
    def delete_book(cls, _id):
        try:
            return cls.__sql_service.delete_object(cls.__table_name, _id)
        except Exception as e:
            print('Error(BookService) delete_book:', e)
            return False

    @classmethod
    def update_book(cls, _id, new_data):
        try:
            return cls.__sql_service.update_object(cls.__table_name, _id, new_data)
        except Exception as e:
            print('Error(BookService) update_book:', e)
            return False

    @classmethod
    def get_book(cls, field_name, field_value):
        try:
            return cls.__sql_service.get_object_by_(cls.__table_name, field_name, field_value)
        except Exception as e:
            print('Error(BookService) get_book:', e)
            return False
