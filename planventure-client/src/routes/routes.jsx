import Home from '../pages/Home';
import LoginPage from '../pages/LoginPage';
import SignUpPage from '../pages/SignUpPage';
import Dashboard from '../pages/Dashboard';
import DashboardLayout from '../layouts/DashboardLayout';
import NewTripPage from '../pages/NewTripPage';

export const publicRoutes = [
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/login',
    element: <LoginPage />,
  },
  {
    path: '/signup',
    element: <SignUpPage />,
  }
];

export const protectedRoutes = [
  {
    path: '/dashboard',
    element: <DashboardLayout><Dashboard /></DashboardLayout>,
  },
  {
    path: '/trips',
    element: <DashboardLayout><Dashboard /></DashboardLayout>,
  },
  {
    path: '/trips/new',
    element: <DashboardLayout><NewTripPage /></DashboardLayout>,
  }
];