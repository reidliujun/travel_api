import { useState } from 'react'
import { 
  Container,
  Typography,
  Stack,
  Tabs,
  Tab,
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
} from '@mui/material'
import { countries } from '../data/cities'
import CityInfo from '../components/CityInfo'
import AIPlan from '../components/AIPlan'
import TravelDate from '../components/TravelDate'

const TravelPlanner = () => {
  const [country, setCountry] = useState('')
  const [city, setCity] = useState('')
  const [activeTab, setActiveTab] = useState(0)

  const handleCountryChange = (event: any) => {
    setCountry(event.target.value)
    setCity('')
  }

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue)
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h3" component="h1" align="center" sx={{ mb: 4 }}>
        AI Travel Planner
      </Typography>
      
      <Box sx={{ 
        display: 'grid',
        gridTemplateColumns: '300px 1fr',
        gap: 4,
        position: 'relative'
      }}>
        {/* 左侧选择区域 */}
        <Box sx={{ 
          position: 'sticky',
          top: '1rem',
          height: 'fit-content',
          zIndex: 1
        }}>
          <Stack spacing={3}>
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
          </Stack>
        </Box>

        {/* 右侧内容区域 */}
        <Box>
          {city ? (
            <>
              <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs 
                  value={activeTab} 
                  onChange={handleTabChange} 
                  centered
                  variant="fullWidth"
                  TabIndicatorProps={{
                    sx: {
                      display: activeTab === undefined ? 'none' : 'block'
                    }
                  }}
                  sx={{
                    '& .MuiTab-root': {
                      minWidth: 120,
                      '&.Mui-selected': {
                        color: 'primary.main'
                      }
                    },
                    '& .MuiTabs-indicator': {
                      backgroundColor: 'primary.main'
                    }
                  }}
                >
                  <Tab label="城市简介" />
                  <Tab label="AI 旅行计划" />
                  <Tab label="旅行日期" />
                </Tabs>
              </Box>
      
              <Box sx={{ 
                minHeight: '60vh', 
                mt: 3,
                width: '100%',
                maxWidth: '800px',  // 添加最大宽度
                mx: 'auto'          // 居中显示
              }}>
                {activeTab === 0 && <CityInfo city={city} />}
                {activeTab === 1 && <AIPlan city={city} />}
                {activeTab === 2 && <TravelDate city={city} />}
              </Box>
            </>
          ) : (
            <Box 
              sx={{ 
                height: '60vh', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center',
                color: 'text.secondary'
              }}
            >
              <Typography variant="h6">
                请先选择城市
              </Typography>
            </Box>
          )}
        </Box>
      </Box>
    </Container>
  )
}

export default TravelPlanner