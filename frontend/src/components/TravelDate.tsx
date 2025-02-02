import { useState } from 'react'
import { 
  Paper, 
  Stack,
  TextField,
  Typography,
  Box,
  Divider,
  Alert,
  Grid
} from '@mui/material'
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth'

interface TravelDateProps {
  city: string
}

export default function TravelDate({ city }: TravelDateProps) {
  const [startDate, setStartDate] = useState('')
  const [endDate, setEndDate] = useState('')

  return (
    <Paper sx={{ p: 4 }}>
      <Stack spacing={4}>
        <Box display="flex" alignItems="center" gap={2}>
          <CalendarMonthIcon color="primary" />
          <Typography variant="h5">
            旅行日期规划
          </Typography>
        </Box>

        <Grid container spacing={2} maxWidth="600px">
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              type="date"
              label="到达日期"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              InputLabelProps={{ shrink: true }}
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              fullWidth
              type="date"
              label="离开日期"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              InputLabelProps={{ shrink: true }}
              inputProps={{
                min: startDate // 防止选择早于到达日期的离开日期
              }}
            />
          </Grid>
        </Grid>

        <Divider />

        <Box>
          <Typography variant="h6" gutterBottom color="primary">
            天气预报
          </Typography>
          <Alert severity="info">
            天气预报功能开发中，敬请期待...
          </Alert>
        </Box>

        <Divider />

        <Box>
          <Typography variant="h6" gutterBottom color="primary">
            当地活动
          </Typography>
          <Alert severity="info">
            活动信息功能开发中，敬请期待...
          </Alert>
        </Box>
      </Stack>
    </Paper>
  )
}