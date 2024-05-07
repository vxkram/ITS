/* eslint-disable no-undef */
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const authModel = require('./models/auth');

const app = express();
app.use(express.json());
app.use(cors());

mongoose.connect('mongodb://localhost:27017/auth');

app.post('/register', (req, res) => {
	authModel
		.create(req.body)
		.then((admin) => res.json(admin))
		.catch((err) => res.json(err));
});

app.listen(3001, () => {
	console.log('server');
});
