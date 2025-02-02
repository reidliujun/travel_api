import { Paper, Typography } from '@mui/material'

interface CityInfoProps {
  city: string
}

const CityInfo = ({ city }: CityInfoProps) => {
  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h5" gutterBottom>
        城市简介
      </Typography>
      {/* 这里添加城市简介的内容 */}
    </Paper>
  )
}

export default CityInfo