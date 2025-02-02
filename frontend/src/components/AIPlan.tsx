import { useState } from 'react'
import { 
  Paper,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  Stack,
  Alert,
  CircularProgress
} from '@mui/material'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { getTravelPlan } from '../api/travel'

interface AIPlanProps {
  city: string
}

const AIPlan = ({ city }: AIPlanProps) => {
  const [days, setDays] = useState('3')
  const [type, setType] = useState('normal')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [plan, setPlan] = useState('')

  const handleSubmit = async () => {
    setLoading(true)
    setError('')
    setPlan('')
    
    try {
      const response = await getTravelPlan(city, Number(days), type)
      setPlan(response.markdown_content)
    } catch (err) {
      setError('获取旅行计划失败，请稍后重试')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Stack spacing={3}>
      <FormControl fullWidth>
        <InputLabel>旅行天数</InputLabel>
        <Select
          value={days}
          label="旅行天数"
          onChange={(e) => setDays(e.target.value)}
        >
          {[1,2,3,4,5,6,7].map(d => (
            <MenuItem key={d} value={d}>{d} 天</MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel>旅行模式</InputLabel>
        <Select
          value={type}
          label="旅行模式"
          onChange={(e) => setType(e.target.value)}
        >
          <MenuItem value="luxury">奢华</MenuItem>
          <MenuItem value="normal">标准</MenuItem>
          <MenuItem value="budget">经济</MenuItem>
        </Select>
      </FormControl>

      <Button 
        variant="contained" 
        size="large"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? <CircularProgress size={24} color="inherit" /> : '生成旅行计划'}
      </Button>

      {error && <Alert severity="error">{error}</Alert>}

      {plan && (
        <Paper sx={{ p: 2 }}>
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {plan}
          </ReactMarkdown>
        </Paper>
      )}
    </Stack>
  )
}

export default AIPlan