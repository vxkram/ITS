import { Card, CardContent, Grid, Typography } from '@mui/material';
import React from 'react';

const Decisions = () => {
	return (
		<Grid
			container
			spacing={0}
			direction="column"
			alignItems="center"
			justify="center"
			style={{ minHeight: '100vh' }}
		>
			<Card>
				<CardContent sx={{ minWidth: 1300, minHeight: 650 }}>
					<Typography variant="h6">Decisions Page</Typography>
					<Typography>You have reached the decisions page.</Typography>
				</CardContent>
			</Card>
		</Grid>
	);
};

export default Decisions;
