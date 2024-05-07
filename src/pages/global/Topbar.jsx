import {
	DarkModeOutlined,
	LightModeOutlined,
	NotificationsOutlined,
	PersonOutlineOutlined,
	SearchOutlined,
	SettingsOutlined,
} from "@mui/icons-material";
import { Box, Icon, IconButton, InputBase, useTheme } from "@mui/material";
import React, { useContext } from "react";
import { ColorModeContext, tokens } from "../../theme";

const topbar = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const colorMode = useContext(ColorModeContext);

	return (
		<Box display="flex" justifyContent="space-between" p={2}>
			{/*Search bar*/}
			<Box
				display="flex"
				backgroundcolor={colors.secondary[600]}
				borderRadius="3px"
			>
				{/* <InputBase
					sx={{ ml: 2, flex: 1 }}
					placeholder="Search"
					color={colors.primary[400]}
				/>
				<IconButton type="button" sx={{ p: 1 }}>
					<SearchOutlined />
				</IconButton> */}
			</Box>
			{/*Icons*/}
			<Box display="flex">
				<IconButton onClick={colorMode.toggleColorMode}>
					{theme.palette.mode === "dark" ? (
						<DarkModeOutlined />
					) : (
						<LightModeOutlined />
					)}
				</IconButton>
				<IconButton>
					<NotificationsOutlined />
				</IconButton>
				<IconButton>
					<SettingsOutlined />
				</IconButton>
				<IconButton>
					<PersonOutlineOutlined />
				</IconButton>
			</Box>
		</Box>
	);
};

export default topbar;
