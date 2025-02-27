import { AppBar, Box, Toolbar, Typography, Button, Stack } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  return (
    <AppBar position="fixed">
      <Toolbar>
        <Typography 
          variant="h6" 
          component="div" 
          sx={{ flexGrow: 1, cursor: 'pointer', textAlign: 'left' }}
          onClick={() => navigate('/')}
        >
          Planventure
        </Typography>
        <Stack direction="row" spacing={2}>
          <Button color="inherit" onClick={() => navigate('/login')}>
            Login
          </Button>
          <Button 
            color="inherit" 
            variant="outlined" 
            onClick={() => navigate('/signup')}
            sx={{ borderColor: 'inherit' }}
          >
            Sign Up
          </Button>
        </Stack>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;