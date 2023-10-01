from abc import ABC, abstractmethod


class IContactService(ABC):

    @abstractmethod
    def create_contact(self, data):
        pass

    @abstractmethod
    def get_contacts(self, fields=None, filters=None):
        pass

    @abstractmethod
    def delete_contact(self, _id):
        pass

    @abstractmethod
    def update_contact(self, _id, new_data):
        pass

    @abstractmethod
    def get_contact(self, field_name, field_value):
        pass
