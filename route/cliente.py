from flask import Blueprint, redirect, url_for, request, render_template

# Criação do Blueprint
cliente = Blueprint('cliente', __name__)

#banco de dado em formato gambiarra
lista = []

@cliente.route('/register', methods = ['GET'])
def register_form():
    return render_template('register.html')

@cliente.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    lista.append({'username': username, 'email': email, 'password': password})

    print('cadastrado!')
    return redirect(url_for('index'))

@cliente.route('/login', methods = ['GET'])
def login_form():
    return render_template('login.html')

@cliente.route('/login', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    #verificar senha!
    for user in lista:
            if user['username'] == username and user['password'] == password:
                print('tudo certo!')
                return redirect(url_for('main'))
            else:
                print('tudo errado!')
                return render_template('login.html')
            
@cliente.route('/main<id>', methods = ['GET'])
def main_create(id):
     
