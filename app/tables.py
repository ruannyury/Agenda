from app import db
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


'''class AddUSer:
    def __init__(self, user):
        self._list_users = [User_('ruannyury1@outlook.com', 'admin', 'admin', 'Administrador')]
        self._user = user

    def add_usuario(self):
        self._list_users.append(self._user)


class User_:
    def __init__(self, email, username, password, name):
        self._email = email
        self._username = username
        self._password = password
        self._name = name

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name'''


class AddressBook:
    def __init__(self, name):
        self._name = name
        self._contact = ""
        self._contacts = []

    def get_name(self):
        return self._name

    def get_contact_by_name(self, name):
        for contact in self._contacts:
            if name == contact.get_name():
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
    def __init__(self, id, name, email, number, address):
        self._id = id
        self._email = email
        self._number = number
        self._name = name
        self._address = address

    def get_id(self):
        return self._id

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
