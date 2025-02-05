import { Paper, Typography, CircularProgress, Alert } from '@mui/material'
import { getCityInfo } from '../api/travel'
import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'

interface CityInfoProps {
  city: string
}

const CityInfo = ({ city }: CityInfoProps) => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [cityInfo, setCityInfo] = useState('')

  useEffect(() => {
    const fetchCityInfo = async () => {
      setLoading(true)
      setError('')
      
      try {
        const response = await getCityInfo(city)
        setCityInfo(response.content)
      } catch (err) {
        setError('获取城市信息失败，请稍后重试')
      } finally {
        setLoading(false)
      }
    }

    if (city) {
      fetchCityInfo()
    }
  }, [city])

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h5" gutterBottom>
        城市简介
      </Typography>
      
      {loading && (
        <CircularProgress />
      )}
      
      {error && (
        <Alert severity="error">{error}</Alert>
      )}
      
      {cityInfo && (
        <ReactMarkdown>
          {cityInfo}
        </ReactMarkdown>
      )}
    </Paper>
  )
}

export default CityInfo