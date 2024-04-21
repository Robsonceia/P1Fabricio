from flask import Blueprint, jsonify, request
from appflask.app import db
from models.user import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    email = data.get('email')
    nome = data.get('nome')
    senha = data.get('senha')

    # Verifica se o usuário já existe no banco de dados
    user_existente = User.query.filter_by(email=email).first()
    if user_existente:
        return jsonify({'message': 'Este email já está cadastrado.'}), 400

    # Cria um novo usuário
    novo_usuario = User(nome=nome, email=email, senha=senha)

    # Adiciona o novo usuário ao banco de dados
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({'message': 'Usuário cadastrado com sucesso.'}), 201

  

