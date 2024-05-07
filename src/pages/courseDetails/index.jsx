import {
	Box,
	Button,
	Card,
	CardContent,
	CardMedia,
	Grid,
	Stack,
	Typography,
	useTheme,
} from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router-dom';
import { tokens } from '../../theme';
// Import the image using a relative path
import databaseImage from '../../assets/database.jpg';

const Details = () => {
	const navigate = useNavigate();
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	return (
		<div>
			<Grid
				container
				spacing={0}
				direction="column"
				alignItems="center"
				justify="center"
				style={{ minHeight: '100vh' }}
			>
				<Grid item xs={3}>
					<Card>
						<CardContent sx={{ minWidth: 1300, minHeight: 650 }}>
							<Stack direction="row">
								<Stack direction="column">
									<Typography
										variant="h1"
										fontWeight="bold"
										sx={{ padding: 2 }}
									>
										Database Management
									</Typography>
									<Typography
										fontSize={20}
										sx={{ maxWidth: 650, padding: 2, paddingBottom: 25 }}
									>
										This comprehensive online course unlocks the secrets of data
										organization and manipulation. Explore how databases
										efficiently store information for easy retrieval and
										analysis. Learn to design databases, craft powerful SQL
										queries, and ensure the smooth operation of your data
										systems - all at your own pace. This course equips you with
										the skills to thrive in today&apos;s data-driven world, and
										can be conveniently accessed from anywhere with an internet
										connection!
									</Typography>
									<Button
										variant="contained"
										color="success"
										sx={{ paddingY: 2 }}
										onClick={() => navigate('/quiz')}
									>
										Take a quick quiz
									</Button>
								</Stack>
								<CardMedia
									component="img"
									height="500"
									width="40"
									image={databaseImage}
									alt="database"
								/>
							</Stack>
						</CardContent>
					</Card>
				</Grid>
			</Grid>
		</div>
	);
};

export default Details;
