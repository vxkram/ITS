import {
	Box,
	Button,
	Card,
	CardContent,
	FormControl,
	FormControlLabel,
	FormLabel,
	Radio,
	RadioGroup,
	Typography,
} from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const Quiz2 = () => {
	const [questions, setQuestions] = useState([]);
	const [answers, setAnswers] = useState({});
	const [score, setScore] = useState(null);

	useEffect(() => {
		// Fetch quiz questions
		const fetchQuestions = async () => {
			try {
				const { data } = await axios.get('http://localhost:8000/quiz_2/');
				setQuestions(data);
			} catch (error) {
				console.error('Failed to fetch questions:', error);
			}
		};

		fetchQuestions();
	}, []);

	const handleAnswerChange = (questionIdx, option) => {
		setAnswers({ ...answers, [questionIdx]: option });
	};

	const handleSubmit = async () => {
		try {
			const { data } = await axios.post(
				'http://localhost:8000/quiz_2/evaluate/',
				{ answers }
			);
			setScore(data.score);
		} catch (error) {
			console.error('Failed to submit quiz:', error);
		}
	};

	if (score !== null) {
		return (
			<Typography variant="h4" sx={{ mt: 4, textAlign: 'center' }}>
				Your score: {score}%
			</Typography>
		);
	}

	return (
		<Box
			sx={{
				mt: 4,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
			}}
		>
			{questions.map((question, idx) => (
				<Card key={idx} sx={{ mb: 2, minWidth: 275 }}>
					<CardContent>
						<FormControl component="fieldset">
							<FormLabel component="legend">{question.question}</FormLabel>
							<RadioGroup
								aria-label="quiz-option"
								name={`quiz-option-${idx}`}
								value={answers[idx] || ''}
								onChange={(e) => handleAnswerChange(idx, e.target.value)}
							>
								{question.options.map((option, optionIdx) => (
									<FormControlLabel
										key={optionIdx}
										value={option}
										control={<Radio />}
										label={option}
									/>
								))}
							</RadioGroup>
						</FormControl>
					</CardContent>
				</Card>
			))}
			<Button
				variant="contained"
				color="primary"
				onClick={handleSubmit}
				sx={{ mt: 2 }}
			>
				Submit
			</Button>
		</Box>
	);
};

export default Quiz2;
