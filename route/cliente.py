from flask import Blueprint, redirect, url_for, request, render_template, flash
import bcrypt

# Criação do Blueprint
cliente = Blueprint('cliente', __name__)

#banco de dado em formato gambiarra
lista = [{'username' : 'MisterCrag1', 'email' : 'vinicanal604@gmail.com1', 'password' : '123'}]

@cliente.route('/register', methods = ['GET'])
def register_form():
    return render_template('register.html')

@cliente.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password').encode('utf-8')

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    for a in lista:
        if username == a['username']:
             print('Oque esta errado!')
             return redirect(url_for('cliente.register_form'))
    
    lista.append({'username': username, 'email': email, 'password': hashed_password})
    print(lista)
    return redirect(url_for('index'))

@cliente.route('/login', methods = ['GET'])
def login_form():
    return render_template('login.html')

@cliente.route('/login', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password').encode('utf-8')

    #verificar senha!
    for user in lista:
        if user['username'] == username and bcrypt.checkpw(password, user['password']):
            print('tudo certo!')
            return redirect(url_for('main_page'))
        else:
            print('tudo errado!')
        
    return redirect(url_for('cliente.login_form'))
        