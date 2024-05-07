// import {
// 	Box,
// 	Card,
// 	CardActionArea,
// 	CardContent,
// 	CardMedia,
// 	Grid,
// 	Typography,
// } from '@mui/material';
// import React from 'react';

// const LearningMethods = () => {
// 	const methods = [
// 		{ title: 'Text Based Learning', imageName: 'text based learning.png' },
// 		{ title: 'Gamified!', imageName: 'gamified.png' },
// 		{ title: 'Video Based Learning', imageName: 'video based learning.png' },
// 	];

// 	const cardHeight = {
// 		width: '100%', // Card width is 100% of the grid column
// 		maxWidth: '1500px', // Maximum width of the card, adjust as needed
// 		height: '600px', // Fixed height of the card
// 		m: 'auto', // Centers the card in the grid column if the column is wider than the card
// 	};

// 	return (
// 		<Box sx={{ flexGrow: 1, p: 2 }}>
// 			<Grid container spacing={2} justifyContent="center" alignItems="stretch">
// 				{methods.map((method, index) => (
// 					<Grid item xs={12} sm={4} key={index} sx={{ display: 'flex' }}>
// 						<Card
// 							sx={{
// 								display: 'flex',
// 								flexDirection: 'column',
// 								justifyContent: 'space-between',
// 								width: '100%',
// 								height: '100%',
// 							}}
// 						>
// 							<Typography variant="h3" textAlign="center">
// 								{method.title}
// 							</Typography>
// 							<CardActionArea
// 								sx={{
// 									bjectFit: 'contain', // Keeps the aspect ratio and fits the image within the frame
// 									maxWidth: '80%', // Sets the maximum width of the image to 80% of the card width
// 									maxHeight: '80%', // Sets the maximum height of the image to 80% of the card height
// 									width: 'auto', // Allows the image width to be auto-adjusted
// 									height: 'auto', // Allows the image height to be auto-adjusted
// 									margin: 'auto',
// 									flexDirection: 'column',
// 								}}
// 							>
// 								<CardMedia
// 									component="img"
// 									image={`http://127.0.0.1:8000/static/${method.imageName}`}
// 									alt={method.title}
// 									sx={{
// 										objectFit: 'contain', // Contain the image within the div without cropping
// 										maxHeight: cardHeight, // Set a maximum height for the image
// 									}}
// 								/>
// 								<CardContent
// 									sx={{
// 										flexGrow: 1,
// 										display: 'flex',
// 										alignItems: 'center',
// 										justifyContent: 'center',
// 									}}
// 								>
// 									{/* <Typography variant="h6" textAlign="center">
// 										{method.title}
// 									</Typography> */}
// 								</CardContent>
// 							</CardActionArea>
// 						</Card>
// 					</Grid>
// 				))}
// 			</Grid>
// 		</Box>
// 	);
// };

// export default LearningMethods;

import {
	Box,
	Button,
	Card,
	CardActionArea,
	CardContent,
	CardMedia,
	Grid,
	Typography,
} from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router-dom';

const LearningMethods = () => {
	const navigate = useNavigate();

	const methods = [
		{
			title: 'Text Based Learning',
			imageName: 'text based learning.png',
			navigateTo: '/pdf_sum',
		},
		// {
		// 	title: 'Gamified!',
		// 	imageName: 'gamified.png',
		// 	navigateTo: '/gamified',
		// },
		{
			title: 'Video Based Learning',
			imageName: 'video based learning.png',
			navigateTo: '/content_rec',
		},
	];

	return (
		<Box sx={{ flexGrow: 1, p: 2 }}>
			<Grid container spacing={2} justifyContent="center" alignItems="stretch">
				{methods.map((method, index) => (
					<Grid item xs={12} sm={4} key={index} sx={{ display: 'flex' }}>
						<Card
							sx={{
								width: '100%',
								height: '100%',
								display: 'flex',
								flexDirection: 'column',
							}}
						>
							<CardActionArea
								sx={{ flexGrow: 1 }}
								onClick={() => navigate(method.navigateTo)}
							>
								<CardMedia
									component="img"
									image={`http://127.0.0.1:8000/static/${method.imageName}`}
									alt={method.title}
									sx={{
										objectFit: 'contain',
										maxHeight: '50%', // You can adjust the percentage as needed
									}}
								/>
								<CardContent
									sx={{
										flexGrow: 1,
										display: 'flex',
										alignItems: 'center',
										justifyContent: 'center',
									}}
								>
									<Typography variant="h5" textAlign="center">
										{method.title}
									</Typography>
								</CardContent>
							</CardActionArea>
							<Button
								fullWidth
								variant="contained"
								onClick={() => navigate(method.navigateTo)}
							>
								Start
							</Button>
						</Card>
					</Grid>
				))}
			</Grid>
		</Box>
	);
};

export default LearningMethods;
