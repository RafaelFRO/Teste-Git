from flask import Flask, jsonify, request
app = Flask (__name__)

# Lista de dados utilizar na api

Usuarios = [
{
'id':1,
'nome': 'Darth Maul',
'idade': 52
},
{
'id':2,
'nome': 'Darth Gucci',
'idade': 51
},
{
'id':3,
'nome': 'Darth VZZY',
'idade': 31
}        
]

@app.route('/usuarios', methods=['GET'])
def consultarUsuarios():
    return jsonify (Usuarios)

@app.route('/usuarios/<int:id>', methods=['GET'])
def consultarUsuariosPorId(id):
    for usuarios in usuarios:
        if usuarios.get('id') == id:
            return jsonify (usuarios)
    
app.run(port=8080,host='localhost', debug=True)