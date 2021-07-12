import json

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.jsons.funcs_jsons import carrega_addressbooks, guarda_addressbooks
from app.tables import ClassFactory


views = Blueprint('views', __name__)


def procura(campo, dicionario):
    """
    Função de pesquisa da página Home.
    :param campo:
    :param dicionario:
    :return contato or None:
    """
    for nome, contatos in dicionario.items():
        for contato in contatos:
            for valor in contato.values():
                if campo == valor:
                    return contato

    return None


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == "POST":
        campo = request.form.get('pesquisa')
        addressbok = carrega_addressbooks()

        contato = procura(campo, addressbok)

        if contato is None:
            flash('Contato não encontrado. Tente novamente.', category='error')
            return redirect(url_for('views.home'))

        return render_template('pesquisa.html', user=current_user, contato=contato)

    return render_template('home.html', user=current_user, addressbook=carrega_addressbooks())


def lista_jinja(dicionario, campo):
    """
    Lista os contatos de acordo com o tipo de campo introduzido e retorna-os numa lista.
    :param dicionario:
    :param campo:
    :return list_listagem:
    """
    nome_user = str(current_user.name.lower())
    list_listagem = []

    for contato in dicionario[nome_user]:
        list_listagem.append(contato[campo])

    return list_listagem


@views.route('/listar', methods=['GET', 'POST'])
@login_required
def listar():
    if request.method == 'POST':

        addressbook = carrega_addressbooks()
        campo = request.form.get('campo')

        list_listagem = lista_jinja(addressbook, campo)

        return render_template('listagem.html', user=current_user, listagem=list_listagem)

    return render_template('listagem_form.html', user=current_user)


@views.route('/inserir', methods=['GET', 'POST'])
@login_required
def inserir():
    if request.method == "POST":

        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')

        new_contact = ClassFactory.build_obj(2, name, email, number, address)

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

        contact = ClassFactory.build_obj(2, name, email, number, address)

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

        new_contact = ClassFactory.build_obj(2, name, email, number, address)

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
