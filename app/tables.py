from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
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

    def guarda_usario(self):
        pass

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    # Os sets das classes abaixo servem para alterar algum dado que tenha sido passado no construtor
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password


class AddressBook:

    def __init__(self, name):
        self._name = name
        self._contact = ""
        self._contacts = [{"Teste": "Teste"}]

    def to_json(self):
        return self._contacts

    def guarda_addressbook(self, contato):
        pass

    def get_name(self):
        return self._name

    def get_contact_by_name(self, name):
        for contact in self._contacts:
            if name == contact["name"]:
                return contact

    def get_contacts(self):
        return self._contacts

    def insert_contact(self, contact):
        self._contacts.append(contact)

    def set_name(self, name):
        self._name = name


class ContactGroup:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Contact:

    def __init__(self, name, email, number, address):
        self._email = email
        self._number = number
        self._name = name
        self._address = address

    def to_json(self):
        return {
            "name": self._name,
            "email": self._email,
            "number": self._number,
            "address": self._address
        }

    def get_email(self):
        return self._email

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def set_email(self, email):
        self._email = email

    def set_number(self, number):
        self._number = number

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address
