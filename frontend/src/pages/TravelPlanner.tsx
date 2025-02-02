import { useState } from 'react'
import { 
  Container,
  Typography,
  Button,
  Stack,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Paper,
  CircularProgress,
  Alert
} from '@mui/material'
import ReactMarkdown from 'react-markdown'  // Changed from { ReactMarkdown }
import remarkGfm from 'remark-gfm'
import '../styles/markdown.css'

import { getTravelPlan } from '../api/travel'
import { countries } from '../data/cities'

const TravelPlanner = () => {
  const [country, setCountry] = useState('')
  const [city, setCity] = useState('')
  const [days, setDays] = useState('3')
  const [type, setType] = useState('normal')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [plan, setPlan] = useState('')

  const handleCountryChange = (event: any) => {
    setCountry(event.target.value)
    setCity('') // Reset city when country changes
  }

  const handleSubmit = async () => {
    if (!city) {
      setError('请选择城市')
      return
    }
    
    setLoading(true)
    setError('')
    setPlan('')
    
    try {
      // 直接使用城市的 value 值，不需要转拼音
      const response = await getTravelPlan(city, Number(days), type)
      setPlan(response.markdown_content)
    } catch (err) {
      setError('获取旅行计划失败，请稍后重试')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Stack spacing={4}>
        <Typography variant="h3" component="h1" align="center">
          AI Travel Planner
        </Typography>
        
        <FormControl fullWidth>
          <InputLabel>选择国家</InputLabel>
          <Select
            value={country}
            label="选择国家"
            onChange={handleCountryChange}
          >
            {countries.map((country) => (
              <MenuItem key={country.label} value={country.label}>
                {country.label}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <FormControl fullWidth>
          <InputLabel>选择城市</InputLabel>
          <Select
            value={city}
            label="选择城市"
            onChange={(e) => setCity(e.target.value)}
            disabled={!country}
          >
            {country && countries
              .find(c => c.label === country)?.cities
              .map((city) => (
                <MenuItem key={city.value} value={city.value}>
                  {city.label}
                </MenuItem>
              ))
            }
          </Select>
        </FormControl>

        {/* 移除 TextField 输入框 */}

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
          fullWidth
          disabled={loading}
        >
          {loading ? <CircularProgress size={24} color="inherit" /> : '生成旅行计划'}
        </Button>

        {error && (
          <Alert severity="error">{error}</Alert>
        )}

        {plan && (
          <Paper 
            elevation={3} 
            sx={{ 
              p: 2,
              backgroundColor: '#ffffff',
              borderRadius: 2
            }}
          >
            <ReactMarkdown 
              className="markdown-content"
              remarkPlugins={[remarkGfm]}
            >
              {plan}
            </ReactMarkdown>
          </Paper>
        )}
      </Stack>
    </Container>
  )
}

export default TravelPlanner