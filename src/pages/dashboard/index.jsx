import { Box, Container } from "@mui/material";
import React from "react";
import { default as ContinueLearning } from "../../components/ContinueLearning";
import { default as FeaturedCourses } from "../../components/FeaturedCourses";
import Header from "../../components/Header";
import Sidebar from "../global/Sidebar";

const Dashboard = () => {
	return (
		<Box m="20px">
			<Box
				display="flex"
				justifyContent="space-between"
				alignItems="center"
			></Box>
			<Header title="Featured Courses" />
			<FeaturedCourses />
			<Header />
			<Header title="Continue Learning" />
			<ContinueLearning />
		</Box>
	);
};

export default Dashboard;
