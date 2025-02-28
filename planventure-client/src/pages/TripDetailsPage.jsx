import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Box,
  Paper,
  Typography,
  Tabs,
  Tab,
  Button,
  Skeleton,
  Alert,
  Chip,
  Stack,
  Divider
} from '@mui/material';
import {
  AccessTime,
  LocationOn,
  Edit as EditIcon,
  ArrowBack as ArrowBackIcon
} from '@mui/icons-material';
import { tripService } from '../services/tripService';
import dayjs from 'dayjs';

const TabPanel = ({ children, value, index }) => (
  <div hidden={value !== index} style={{ padding: '24px 0' }}>
    {value === index && children}
  </div>
);

const TripDetailsPage = () => {
  const { tripId } = useParams();
  const navigate = useNavigate();
  const [trip, setTrip] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [tabValue, setTabValue] = useState(0);

  useEffect(() => {
    const fetchTripDetails = async () => {
      try {
        setLoading(true);
        const response = await tripService.getTrip(tripId);
        console.log('TripDetailsPage received:', response);

        if (!response || !response.trip) {
          throw new Error('Trip not found');
        }

        setTrip(response.trip);
      } catch (err) {
        console.error('Error fetching trip:', err);
        setError(err.message || 'Failed to load trip details');
      } finally {
        setLoading(false);
      }
    };

    if (tripId) {
      fetchTripDetails();
    }
  }, [tripId]);

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  if (loading) {
    return (
      <Box sx={{ maxWidth: 1200, mx: 'auto', p: 3 }}>
        <Skeleton variant="text" height={40} width={200} />
        <Skeleton variant="rectangular" height={200} sx={{ mt: 2 }} />
      </Box>
    );
  }

  if (error) {
    return (
      <Box sx={{ maxWidth: 1200, mx: 'auto', p: 3 }}>
        <Alert 
          severity="error"
          action={
            <Button color="inherit" size="small" onClick={() => navigate('/dashboard')}>
              Back to Dashboard
            </Button>
          }
        >
          {error}
        </Alert>
      </Box>
    );
  }

  if (!trip) {
    return (
      <Box sx={{ maxWidth: 1200, mx: 'auto', p: 3 }}>
        <Alert severity="error">
          Trip not found
        </Alert>
      </Box>
    );
  }

  return (
    <Box sx={{ maxWidth: 1200, mx: 'auto', p: 3 }}>
      <Button
        startIcon={<ArrowBackIcon />}
        onClick={() => navigate('/dashboard')}
        sx={{ mb: 3 }}
      >
        Back to Dashboard
      </Button>

      <Paper elevation={2} sx={{ p: 3, mb: 3 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 3 }}>
          <Box>
            <Typography variant="h4" gutterBottom>
              {trip.title}
            </Typography>
            <Stack direction="row" spacing={2} alignItems="center">
              <Chip
                icon={<LocationOn />}
                label={trip.destination}
                color="primary"
                variant="outlined"
              />
              <Chip
                icon={<AccessTime />}
                label={`${dayjs(trip.start_date).format('MMM D')} - ${dayjs(trip.end_date).format('MMM D, YYYY')}`}
                variant="outlined"
              />
            </Stack>
          </Box>
          <Button
            variant="outlined"
            startIcon={<EditIcon />}
            onClick={() => navigate(`/trips/${tripId}/edit`)}
          >
            Edit Trip
          </Button>
        </Box>

        <Divider sx={{ my: 2 }} />

        <Tabs value={tabValue} onChange={handleTabChange} sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tab label="Overview" />
          <Tab label="Itinerary" />
          <Tab label="Expenses" />
          <Tab label="Notes" />
        </Tabs>

        <TabPanel value={tabValue} index={0}>
          <Box>
            <Typography variant="h6" gutterBottom>
              Trip Overview
            </Typography>
            {/* Add overview content */}
          </Box>
        </TabPanel>

        <TabPanel value={tabValue} index={1}>
          <Box>
            <Typography variant="h6" gutterBottom>
              Itinerary
            </Typography>
            {/* Add itinerary content */}
          </Box>
        </TabPanel>

        <TabPanel value={tabValue} index={2}>
          <Box>
            <Typography variant="h6" gutterBottom>
              Expenses
            </Typography>
            {/* Add expenses content */}
          </Box>
        </TabPanel>

        <TabPanel value={tabValue} index={3}>
          <Box>
            <Typography variant="h6" gutterBottom>
              Notes
            </Typography>
            {/* Add notes content */}
          </Box>
        </TabPanel>
      </Paper>
    </Box>
  );
};

export default TripDetailsPage;
