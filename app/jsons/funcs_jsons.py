import os
import json


def procura_usuarios(dicionario, nome):
    chave_achada = False
    for chave in dicionario:
        if chave is None:
            return chave_achada
        elif chave.startswith(nome):
            chave_achada = nome
        return chave_achada


def procura_emails(dicionario, email):
    email_achado = False
    for valor in dicionario.values():
        if valor is None:
            return email_achado
        elif valor.get_email() == email:
            email_achado = email
        return email_achado


def procura_username(dicionario, username, retornar_objeto_usuario=False):
    username_achado = False
    for valor in dicionario.values():
        if valor is None:
            return username_achado
        elif valor.get_username() == username:
            username_achado = username
            if retornar_objeto_usuario:
                return valor
        return username_achado


def carrega_addressbooks():
    addressbooks = {
        "admin": []  # Contatos do admin
    }

    if os.path.exists('addressbooks.json'):
        with open('addressbooks.json', 'r', encoding='utf8') as f:
            addressbooks = json.load(f)

    return addressbooks


def guarda_addressbooks(addressbooks):
    with open('addressbooks.json', 'w', encoding='utf8') as f:
        json.dump(addressbooks, f, indent=4, ensure_ascii=False)
