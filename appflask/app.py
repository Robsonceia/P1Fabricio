from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://rco90rc:1234@cluster0.lpndyo9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['Projeto2']
colecao = db['rco90rc']

from models.user import User

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'password': user.password} for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



