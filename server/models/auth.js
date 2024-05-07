/* eslint-disable no-undef */
const mongoose = require('mongoose');

const authSchema = new mongoose.Schema({
	Name: String,
	Email: String,
	Password: String,
});

const authModel = mongoose.model('admin', authSchema);
module.exports = authModel;
