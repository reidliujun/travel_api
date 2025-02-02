import axios from 'axios'

const API_URL = 'http://localhost:8000'

interface TravelPlanResponse {
  metadata: {
    city: string
    days: number
    type: string
    format: string
  }
  itinerary: string
}

export const getTravelPlan = async (city: string, days: number, type: string) => {
  const response = await axios.get<TravelPlanResponse>(`${API_URL}/${city}?days=${days}&type=${type}`)
  return {
    ...response.data,
    markdown_content: response.data.itinerary
  }
}

const getTypeText = (type: string) => {
  switch (type) {
    case 'luxury': return '奢华'
    case 'normal': return '标准'
    case 'budget': return '经济'
    default: return ''
  }
}