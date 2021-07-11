import json

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.jsons.funcs_jsons import carrega_addressbooks, guarda_addressbooks
from app.tables import Contact


views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == "POST":
        pesquisa = request.form.get('pesquisa').upper()
        print(pesquisa)

    return render_template('home.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/inserir', methods=['GET', 'POST'])
@login_required
def inserir():
    if request.method == "POST":

        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')

        new_contact = Contact(name, email, number, address)

        addressbook = carrega_addressbooks()

        nome_user = str(current_user.name.lower())
        for nome, contatos in addressbook.items():
            if nome == nome_user:
                contatos.append(new_contact.to_json())
                guarda_addressbooks(addressbook)
        flash('Contato adicionado!', category='sucess')
        return redirect(url_for('views.home'))

    return render_template('inserir.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/update', methods=['GET', 'POST'])
@views.route('/atualizar', methods=['GET', 'POST'])
@login_required
def atualizar():

    if request.method == "POST":
        dado = json.loads(request.data)
        contact = dado['contato']
        print(contact)
        addressbook = carrega_addressbooks()

        nome_user = str(current_user.name.lower())

        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')

        new_contact = Contact(name, email, number, address)

        for nome, contatos in addressbook.items():
            if nome == nome_user and contatos == contact:
                print(contact)
                print(contatos)
                contatos.remove(contact)
                contatos.append(new_contact.to_json())
                guarda_addressbooks(addressbook)

        return redirect(url_for('views.home'))

    return render_template('atualizar.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/delete-contact', methods=['POST'])
def deletecontact():
    dado = json.loads(request.data)
    contact = dado['contato']
    addressbook = carrega_addressbooks()

    nome_user = str(current_user.name.lower())
    for nome, contatos in addressbook.items():
        if nome == nome_user:
            contatos.remove(contact)
            guarda_addressbooks(addressbook)

    return jsonify({})
