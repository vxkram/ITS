import { Dashboard, Flare } from '@mui/icons-material';
import { Box, Button, TextField, Typography, useTheme } from '@mui/material';
import React, { useState } from 'react';
import { Route, useNavigate } from 'react-router-dom';
import { tokens } from '../../theme';

const Login = (props) => {
	const navigate = useNavigate();
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);

	return (
		<div>
			<form>
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
						Login
					</Typography>
					<TextField
						sx={{ minWidth: 300 }}
						type={'email'}
						margin="dense"
						variant="outlined"
						placeholder="Email"
					/>
					<TextField
						sx={{ minWidth: 300 }}
						type={'password'}
						margin="dense"
						variant="outlined"
						placeholder="Password"
					/>
					<Box display="flex" flexDirection={'row'}>
						<Button
							variant="contained"
							color="success"
							sx={{ marginTop: 2, borderRadius: 1, margin: 2 }}
							onClick={() => navigate('/register')}
						>
							Sign Up
						</Button>
						<Button
							variant="contained"
							color="success"
							sx={{ marginTop: 2, borderRadius: 1, margin: 2 }}
							onClick={() => navigate('/dashboard')}
						>
							Login
						</Button>
					</Box>
				</Box>
			</form>
		</div>
	);
};

export default Login;
