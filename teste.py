lista = [{'username' : 'MisterCrag', 'email' : 'vinicanal604@gmail.com', 'password' : '123'}, {'username' : 'vinicius', 'email' : 'sinicanal604@gmail.com', 'password' : '321'}]

username = 'vinicius'


for a in lista:
    if username in a['username']:
        print('1')