const User = require('../models/userModel');

class UserRepository {
    async createUser(nome, email, senha) {
        return await User.create({ nome, email, senha });
    }
}

module.exports = new UserRepository();
