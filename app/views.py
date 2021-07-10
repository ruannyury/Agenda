from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app.jsons.funcs_jsons import carrega_addressbooks


views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == "POST":
        pesquisa = request.form.get('pesquisa').upper()
        print(pesquisa)

    return render_template('home.html', user=current_user, addressbook=carrega_addressbooks())
