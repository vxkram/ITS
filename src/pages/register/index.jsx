import { Dashboard, Flare } from '@mui/icons-material';
import { Box, Button, TextField, Typography, useTheme } from '@mui/material';
import axios from 'axios';
import React, { useState } from 'react';
import { Route, useNavigate } from 'react-router-dom';
import { tokens } from '../../theme';

const Register = (props) => {
	const navigate = useNavigate();
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [name, setName] = useState();
	const [email, setEmail] = useState();
	const [password, setPassword] = useState();

	const handleSubmit = (e) => {
		e.preventDefault();
		axios.post('http://localhost:3001/register', {
			name: name,
			email: email,
			password: password,
		});
	};

	return (
		<div>
			<form onSubmit={handleSubmit}>
				<Box
					display="flex"
					flexDirection={'column'}
					maxWidth={450}
					alignItems="center"
					justifyContent={'center'}
					margin="auto"
					marginTop={5}
					padding={5}
					borderRadius={2}
					boxShadow={'5px 5px 15px #ccc'}
					color={colors.primary[100]}
				>
					<Typography variant="h3" padding={3} textAlign="center">
						Register
					</Typography>
					<TextField
						sx={{ minWidth: 300 }}
						type={'name'}
						margin="dense"
						variant="outlined"
						placeholder="Name"
						onChange={(e) => setName(e.target.value)}
					/>
					<TextField
						sx={{ minWidth: 300 }}
						type={'email'}
						margin="dense"
						variant="outlined"
						placeholder="Email"
						onChange={(e) => setEmail(e.target.value)}
					/>
					<TextField
						sx={{ minWidth: 300 }}
						type={'password'}
						margin="dense"
						variant="outlined"
						placeholder="Password"
						onChange={(e) => setPassword(e.target.value)}
					/>
					<Box display="flex" flexDirection={'column'}>
						<Button
							variant="contained"
							color="success"
							sx={{ marginTop: 2, borderRadius: 1, margin: 2 }}
							onClick={handleSubmit}
						>
							Sign Up
						</Button>
						<Button
							variant="outlined"
							color="success"
							sx={{ marginTop: 2, borderRadius: 1, margin: 2 }}
							onClick={() => navigate('/login')}
						>
							Login
						</Button>
					</Box>
				</Box>
			</form>
		</div>
	);
};

export default Register;
