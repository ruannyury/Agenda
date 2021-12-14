from app import db
from flask_login import UserMixin
from abc import ABCMeta, abstractmethod


class IClass(metaclass=ABCMeta):
    """
    Superclasse.
    """
    @abstractmethod
    def class_method(self):
        pass


class User(db.Model, UserMixin):
    """
    Sem receber a metaclasse devido a conflitos de heranças.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password
        }

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username


class AddressBook(IClass):

    def __init__(self, name):
        self._name = name
        self._contact = ""
        self._contacts = []

    def class_method(self) -> None:
        print('Class address.')

    def get_name(self):
        return self._name

    def get_contacts(self):
        return self._contacts


class Contact(IClass):

    def __init__(self, name, email, number, address):
        self._email = email
        self._number = number
        self._name = name
        self._address = address

    def class_method(self) -> None:
        print('Class contact.')

    def to_json(self):
        
        return {
            "name": self._name,
            "email": self._email,
            "number": self._number,
            "address": self._address
        }

    def get_email(self):
        return self._email


class ClassFactory:

    @staticmethod
    def build_obj(obj_type, *params) -> AddressBook or Contact:
        if obj_type == 1:
            return AddressBook(*params)
        elif obj_type == 2:
            return Contact(*params)
        return -1
