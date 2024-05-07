// import React, { useEffect, useState } from 'react';
// import { useLocation } from 'react-router-dom';
// import '../pages/global/sidebarStyle.css';

// const ShowNav = ({ children }) => {
// 	const location = useLocation();
// 	const [showNavBar, setShowNavBar] = useState(false);
// 	useEffect(() => {
// 		if (location.pathname === '/register' || location.pathname === '/login') {
// 			setShowNavBar(false);
// 		} else {
// 			setShowNavBar(true);
// 		}
// 	}, [location]);
// 	return <div className="sidebarClassName">{showNavBar && children}</div>;
// };

// export default ShowNav;
