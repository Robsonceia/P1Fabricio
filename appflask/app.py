from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mongodb://rco90rc:<password>@cluster0.lpndyo9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
db = SQLAlchemy(app)

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



