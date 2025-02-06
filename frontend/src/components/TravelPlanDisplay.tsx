import { Paper, Typography, CircularProgress, Alert } from '@mui/material'
import ReactMarkdown from 'react-markdown'

interface TravelPlanDisplayProps {
  content: string
  loading: boolean
  error: string
}

const TravelPlanDisplay = ({ content, loading, error }: TravelPlanDisplayProps) => {
  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h5" gutterBottom>
        行程安排
      </Typography>
      
      {loading && <CircularProgress />}
      
      {error && (
        <Alert severity="error">{error}</Alert>
      )}
      
      {content && (
        <ReactMarkdown>
          {content}
        </ReactMarkdown>
      )}
    </Paper>
  )
}

export default TravelPlanDisplay