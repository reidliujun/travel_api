import { useState } from 'react'
import { 
  Container,
  Typography,
  Stack,
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
  Autocomplete,
  Chip,
  Button,
  Paper,
  Grid
} from '@mui/material'
import { DatePicker } from '@mui/x-date-pickers'
import { countries } from '../data/cities'
import CityInfo from '../components/CityInfo'
import PublicIcon from '@mui/icons-material/Public'
import LocationCityIcon from '@mui/icons-material/LocationCity'
import FlightTakeoffIcon from '@mui/icons-material/FlightTakeoff'
import { getTravelPlan } from '../api/travel'
import TravelPlanDisplay from '../components/TravelPlanDisplay'

const preferenceOptions = [
  { label: '美食', value: 'food' },
  { label: '历史', value: 'history' },
  { label: '拍照打卡', value: 'photo' },
  { label: '亲子活动', value: 'family' },
  { label: '购物', value: 'shopping' },
  { label: '艺术', value: 'art' },
]

// 添加旅行类型选项配置
const typeOptions = [
  { label: '经济', value: 'budget' },
  { label: '标准', value: 'normal' },
  { label: '豪华', value: 'luxury' },
]

const TravelPlanner = () => {
  const [country, setCountry] = useState('')
  const [city, setCity] = useState('')
  const [date, setDate] = useState<Date | null>(null)
  const [days, setDays] = useState(1)
  const [type, setType] = useState('normal')
  const [preferences, setPreferences] = useState<string[]>([])
  const [showCityInfo, setShowCityInfo] = useState(false)
  const [planContent, setPlanContent] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleGeneratePlan = async () => {
    if (!city || !date) return
    
    setLoading(true)
    setError('')
    setPlanContent('')
    setShowCityInfo(false)  // 添加这一行
    
    try {
      const response = await getTravelPlan(city, days, type)
      setPlanContent(response.markdown_content)
    } catch (err) {
      setError('生成行程失败，请稍后重试')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h3" component="h1" align="center" sx={{ mb: 6 }}>
        AI Travel Planner
      </Typography>

      <Grid container spacing={4}>
        <Grid item xs={12} md={6}>
          <Stack spacing={4}>
            {/* 目的地设置 */}
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                目的地设置
              </Typography>
              <Stack spacing={3}>
                <FormControl fullWidth>
                  <InputLabel>
                    <PublicIcon sx={{ mr: 1 }} />
                    选择国家
                  </InputLabel>
                  <Select
                    value={country}
                    label="选择国家"
                    onChange={(e) => {
                      setCountry(e.target.value)
                      setCity('')
                    }}
                  >
                    {countries.map((country) => (
                      <MenuItem key={country.label} value={country.label}>
                        {country.label}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>

                <Autocomplete
                  value={city ? countries
                    .find(c => c.label === country)
                    ?.cities.find(c => c.value === city) || null : null}
                  onChange={(_, newValue) => {
                    setCity(newValue?.value || '')
                    if (newValue) {
                      setShowCityInfo(true)
                    }
                  }}
                  options={country ? countries.find(c => c.label === country)?.cities || [] : []}
                  getOptionLabel={(option) => option.label || ''}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      label={
                        <Box sx={{ display: 'flex', alignItems: 'center' }}>
                          <LocationCityIcon sx={{ mr: 1 }} />
                          选择城市
                        </Box>
                      }
                    />
                  )}
                  disabled={!country}
                  isOptionEqualToValue={(option, value) => 
                    option?.value === (typeof value === 'string' ? value : value?.value)
                  }
                />
              </Stack>
            </Paper>

            {/* 行程设置 */}
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                行程设置
              </Typography>
              <Stack spacing={3}>
                <DatePicker
                  label="出发日期"
                  value={date}
                  onChange={(newValue) => setDate(newValue)}
                />

                <FormControl fullWidth>
                  <InputLabel>旅行天数</InputLabel>
                  <Select
                    value={days}
                    label="旅行天数"
                    onChange={(e) => setDays(Number(e.target.value))}
                  >
                    {[1,2,3,4,5,6,7].map(d => (
                      <MenuItem key={d} value={d}>{`${d}天`}</MenuItem>
                    ))}
                  </Select>
                </FormControl>

                <Box>
                  <Typography variant="subtitle1" gutterBottom>
                    旅行类型
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                    {typeOptions.map((option) => (
                      <Chip
                        key={option.value}
                        label={option.label}
                        onClick={() => setType(option.value)}
                        color={type === option.value ? "primary" : "default"}
                      />
                    ))}
                  </Box>
                </Box>

                <Box>
                  <Typography variant="subtitle1" gutterBottom>
                    个性化偏好
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                    {preferenceOptions.map((pref) => (
                      <Chip
                        key={pref.value}
                        label={pref.label}
                        onClick={() => {
                          if (preferences.includes(pref.value)) {
                            setPreferences(preferences.filter(p => p !== pref.value))
                          } else {
                            setPreferences([...preferences, pref.value])
                          }
                        }}
                        color={preferences.includes(pref.value) ? "primary" : "default"}
                      />
                    ))}
                  </Box>
                </Box>
              </Stack>
            </Paper>

            {/* 删除原有的个性化偏好 Paper */}

            <Button
              variant="contained"
              size="large"
              startIcon={<FlightTakeoffIcon />}
              fullWidth
              disabled={!city || !date || loading}
              onClick={handleGeneratePlan}
            >
              {loading ? '生成中...' : '生成智能行程'}
            </Button>
          </Stack>
        </Grid>

        {/* 右侧城市信息 */}
        {/* 右侧内容区域 */}
                <Grid item xs={12} md={6}>
                  <Box sx={{ 
                    position: 'sticky', 
                    top: '2rem',
                  }}>
                    {showCityInfo ? (
                      <CityInfo city={city} />
                    ) : (
                      <TravelPlanDisplay 
                        content={planContent}
                        loading={loading}
                        error={error}
                      />
                    )}
                  </Box>
                </Grid>
      </Grid>
    </Container>
  )
}

export default TravelPlanner