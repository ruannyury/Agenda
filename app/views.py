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

        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')

        contact = Contact(name, email, number, address)

        return redirect(url_for('views.atualizar2', contato=contact.to_json()))

    return render_template('atualizar.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/update2/<contato>', methods=['GET', 'POST'])
@views.route('/atualizar2/<contato>', methods=['GET', 'POST'])
@login_required
def atualizar2(contato):
    if request.method == 'POST':


        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')

        new_contact = Contact(name, email, number, address)

        addressbook = carrega_addressbooks()

        nome_user = str(current_user.name.lower())
        for nome, contatos in addressbook.items():

            if nome == nome_user:

                for contact in contatos:

                    print(contato)
                    print(contact)

                    if str(contact) == str(contato):

                        print('==LOOP PARA ATUALIZAR!==')
                        contatos.remove(contact)
                        contatos.append(new_contact.to_json())

                    guarda_addressbooks(addressbook)

        return redirect(url_for('views.home'))

    return render_template('atualizar2.html', user=current_user)


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
