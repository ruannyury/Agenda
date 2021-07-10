import json

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.jsons.funcs_jsons import carrega_addressbooks, guarda_addressbooks
from app.tables import Contact, User


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
                print(contatos)
                print(addressbook)
                contatos.append(new_contact.to_json())
                guarda_addressbooks(addressbook)
        flash('Contato adicionado!', category='sucess')
        return redirect(url_for('views.home'))

    return render_template('inserir.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/delete', methods=['GET', 'POST'])
@views.route('/apagar', methods=['GET', 'POST'])
@login_required
def apagar():
    if request.method == "POST":
        pass
    return render_template('apagar.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/update', methods=['GET', 'POST'])
@views.route('/atualizar', methods=['GET', 'POST'])
@login_required
def atualizar():
    if request.method == "POST":
        pass
    return render_template('atualizar.html', user=current_user, addressbook=carrega_addressbooks())


@views.route('/delete-contact', methods=['POST'])
def deletecontact():
    contato = json.loads(request.data)
    addressbook = carrega_addressbooks()
    addressbook[current_user.name.lower()].remove(contato)

    return jsonify({})
