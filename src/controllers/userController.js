const userRepository = require('../repositories/userRepository');

exports.registerUser = async (req, res) => {
    try {
        const { nome, email, senha } = req.body;
        const existingUser = await userRepository.findUserByUsername(nome);
        if (existingUser) {
            return res.status(400).json({ message: 'O nome de usuário já existe' });
        }
        await userRepository.createUser(nome, email, senha);
        return res.status(201).json({ message: 'Cadastrado com sucesso' });
    } catch (error) {
        return res.status(500).json({ message: 'Erro do Servidor ' });
    }
};
