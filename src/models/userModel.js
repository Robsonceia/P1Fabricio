const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    nome: { type: String, required: true },
    email: { type: String, unique: true },
    senha: { type: String, required: true }
});

const User = mongoose.model('User', userSchema);

module.exports = User;
