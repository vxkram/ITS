// import { Box, Button, Link, Paper, Typography } from '@mui/material';
// import axios from 'axios';
// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';

// const PdfSum = () => {
// 	const [downloading, setDownloading] = useState(false);
// 	const navigate = useNavigate();

// 	const handleGenerateSummary = async () => {
// 		setDownloading(true);
// 		try {
// 			const response = await axios.get(
// 				'http://localhost:8000/generate-summary/',
// 				{ responseType: 'blob' }
// 			);
// 			const fileURL = window.URL.createObjectURL(new Blob([response.data]));
// 			const fileLink = document.createElement('a');
// 			fileLink.href = fileURL;
// 			fileLink.setAttribute('download', 'DBMS_Enhanced_Summary.pdf');
// 			document.body.appendChild(fileLink);
// 			fileLink.click();
// 		} catch (error) {
// 			console.error('Error generating summary:', error);
// 		} finally {
// 			setDownloading(false);
// 		}
// 	};

// 	return (
// 		<Box
// 			sx={{
// 				padding: 4,
// 				display: 'flex',
// 				flexDirection: 'column',
// 				alignItems: 'center',
// 				gap: 2,
// 			}}
// 		>
// 			{/* Content above the button */}

// 			{/* Additional Resources Tile */}
// 			<Paper
// 				elevation={3}
// 				sx={{
// 					p: 3,
// 					display: 'flex',
// 					flexDirection: 'column',
// 					alignItems: 'center',
// 					maxWidth: 400,
// 				}}
// 			>
// 				<Typography
// 					variant="h6"
// 					gutterBottom
// 					component="div"
// 					sx={{ fontWeight: 'bold' }}
// 				>
// 					Additional Resources
// 				</Typography>
// 				<Link
// 					href="https://www.techtarget.com/searchdatamanagement/definition/database-management-system"
// 					target="_blank"
// 					rel="noopener noreferrer"
// 					underline="hover"
// 					sx={{
// 						color: 'green', // Text color
// 						'&:hover': {
// 							color: 'darkgreen', // Change for your preferred hover color
// 							textDecoration: 'underline',
// 						},
// 						typography: 'body1',
// 						fontWeight: 'bold',
// 					}}
// 				>
// 					The Full PDF
// 				</Link>
// 			</Paper>

// 			{/* Generate Summary Button */}
// 			<Button
// 				variant="contained"
// 				onClick={handleGenerateSummary}
// 				disabled={downloading}
// 				sx={{
// 					bgcolor: 'success.main',
// 					'&:hover': { bgcolor: 'success.dark' },
// 					padding: '10px 20px', // Adjust padding as needed for sizing
// 					typography: 'body1',
// 					fontWeight: 'bold',
// 				}}
// 			>
// 				{downloading ? 'Generating...' : 'Generate Summary'}
// 			</Button>

// 			{/* New Quiz Button */}
// 			<Paper
// 				elevation={3}
// 				sx={{ p: 2, mt: 2, maxWidth: 400, width: '100%', textAlign: 'center' }}
// 			>
// 				<Typography
// 					variant="h6"
// 					gutterBottom
// 					component="div"
// 					sx={{ fontWeight: 'bold' }}
// 				>
// 					Ready for another challenge?
// 				</Typography>
// 				<Button
// 					variant="contained"
// 					onClick={() => navigate('/quiz_2')}
// 					sx={{
// 						bgcolor: 'primary.main',
// 						'&:hover': { bgcolor: 'primary.dark' },
// 						typography: 'body1',
// 						fontWeight: 'bold',
// 					}}
// 				>
// 					<u> Let&apos;s take another quiz </u>
// 				</Button>
// 			</Paper>
// 		</Box>
// 	);
// };

// export default PdfSum;

// import { Box, Button, Paper, TextField, Typography } from '@mui/material';
// import axios from 'axios';
// import React, { useState } from 'react';

// function App() {
// 	const [url, setUrl] = useState('');
// 	const [summary, setSummary] = useState('');
// 	const [error, setError] = useState('');
// 	const [loading, setLoading] = useState(false);

// 	const handleSummarize = async () => {
// 		if (!url) {
// 			setError('Please enter a URL.');
// 			return;
// 		}
// 		setLoading(true);
// 		setError('');
// 		setSummary('');
// 		try {
// 			const response = await axios.post('http://localhost:8000/summarize/', {
// 				url,
// 			});
// 			setSummary(response.data.summary);
// 		} catch (err) {
// 			console.error('Error fetching summary:', err);
// 			setError('Failed to fetch summary. Please check the URL and try again.');
// 		} finally {
// 			setLoading(false);
// 		}
// 	};

// 	return (
// 		<Box sx={{ p: 2 }}>
// 			<Typography variant="h4" gutterBottom>
// 				Website Summarizer
// 			</Typography>
// 			<TextField
// 				fullWidth
// 				label="Enter Website URL"
// 				variant="outlined"
// 				value={url}
// 				onChange={(e) => setUrl(e.target.value)}
// 				sx={{ mb: 2 }}
// 			/>
// 			<Button
// 				variant="contained"
// 				color="primary"
// 				onClick={handleSummarize}
// 				disabled={loading}
// 			>
// 				{loading ? 'Summarizing...' : 'Summarize'}
// 			</Button>
// 			{summary && (
// 				<Paper elevation={3} sx={{ mt: 2, p: 2 }}>
// 					<Typography variant="h6" gutterBottom>
// 						Summary
// 					</Typography>
// 					<Typography>{summary}</Typography>
// 				</Paper>
// 			)}
// 			{error && (
// 				<Typography color="error" sx={{ mt: 2 }}>
// 					{error}
// 				</Typography>
// 			)}
// 		</Box>
// 	);
// }

// export default App;

// import { Box, Button, Paper, TextField, Typography } from '@mui/material';
// import React, { useState } from 'react';

// const PdfSummarizer = () => {
// 	const [file, setFile] = useState(null);
// 	const [summary, setSummary] = useState('');
// 	const [fileName, setFileName] = useState('');

// 	const handleFileChange = (event) => {
// 		setFile(event.target.files[0]);
// 		setFileName(event.target.files[0].name);
// 	};

// 	const handleSummarize = async () => {
// 		if (!file) {
// 			alert('Please upload a PDF file first.');
// 			return;
// 		}

// 		const formData = new FormData();
// 		formData.append('pdf_file', file);

// 		try {
// 			const response = await fetch('http://127.0.0.1:8000/summarize/', {
// 				method: 'POST',
// 				body: formData,
// 			});

// 			if (!response.ok) {
// 				throw new Error('Failed to fetch summary');
// 			}

// 			const result = await response.json();
// 			setSummary(result.summary);
// 		} catch (error) {
// 			console.error('Error:', error);
// 			alert('Error summarizing the PDF.');
// 		}
// 	};

// 	const handleDownload = () => {
// 		const blob = new Blob([file], { type: 'application/pdf' });
// 		const link = document.createElement('a');
// 		link.href = window.URL.createObjectURL(blob);
// 		link.download = fileName;
// 		link.click();
// 	};

// 	return (
// 		<Paper elevation={3} sx={{ padding: 2, margin: 2 }}>
// 			<Typography variant="h5" gutterBottom>
// 				PDF Summarizer
// 			</Typography>
// 			<input
// 				type="file"
// 				accept="application/pdf"
// 				onChange={handleFileChange}
// 				style={{ marginBottom: '10px' }}
// 			/>
// 			<Button
// 				variant="contained"
// 				color="primary"
// 				onClick={handleSummarize}
// 				sx={{ marginRight: 1 }}
// 			>
// 				Summarize
// 			</Button>
// 			<Button
// 				variant="contained"
// 				color="secondary"
// 				onClick={handleDownload}
// 				disabled={!file}
// 			>
// 				Download PDF
// 			</Button>
// 			{summary && (
// 				<Box sx={{ marginTop: 2 }}>
// 					<Typography variant="h6">Summary:</Typography>
// 					<TextField
// 						fullWidth
// 						multiline
// 						minRows={4}
// 						value={summary}
// 						variant="outlined"
// 					/>
// 				</Box>
// 			)}
// 		</Paper>
// 	);
// };

// export default PdfSummarizer;

import {
	Button,
	CircularProgress,
	List,
	ListItem,
	ListItemText,
	Paper,
	Typography,
} from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const PdfList = () => {
	const [pdfs, setPdfs] = useState([]);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState('');

	useEffect(() => {
		setLoading(true);
		axios
			.get('http://127.0.0.1:8000/pdfs')
			.then((response) => {
				setPdfs(response.data);
				setLoading(false);
			})
			.catch((error) => {
				console.error('Error fetching PDFs:', error);
				setError('Failed to fetch PDFs');
				setLoading(false);
			});
	}, []);

	const handleAction = (pdfId, action) => {
		if (action === 'download') {
			window.open(`http://127.0.0.1:8000/download-pdf/${pdfId}`, '_blank');
		} else if (action === 'summarize') {
			axios
				.get(`http://127.0.0.1:8000/summarize-pdf/${pdfId}`)
				.then((response) => {
					alert(`Summary: ${response.data.summary}`);
				})
				.catch((error) => {
					console.error(`Error summarizing PDF: ${error}`);
					alert('Failed to summarize PDF');
				});
		}
	};

	return (
		<Paper style={{ padding: 16 }}>
			{loading && <CircularProgress />}
			{error && <Typography color="error">{error}</Typography>}
			<List>
				{pdfs.map((pdf) => (
					<ListItem key={pdf.id}>
						<ListItemText primary={pdf.title} />
						<Button
							variant="contained"
							color="primary"
							onClick={() => handleAction(pdf.id, 'download')}
						>
							Download
						</Button>
						<Button
							variant="contained"
							color="secondary"
							onClick={() => handleAction(pdf.id, 'summarize')}
							style={{ marginLeft: 8 }}
						>
							Summarize
						</Button>
					</ListItem>
				))}
			</List>
		</Paper>
	);
};

export default PdfList;
