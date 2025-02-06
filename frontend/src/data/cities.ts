export interface CityOption {
  value: string
  label: string
}

export interface CountryData {
  label: string
  cities: CityOption[]
}

export const countries: CountryData[] = [
  {
    label: '中国',
    cities: [
      { value: 'beijing', label: '北京' },
      { value: 'shanghai', label: '上海' },
      { value: 'guangzhou', label: '广州' },
      { value: 'shenzhen', label: '深圳' },
      { value: 'hangzhou', label: '杭州' },
      { value: 'chengdu', label: '成都' },
    ]
  },
  {
    label: '日本',
    cities: [
      { value: 'tokyo', label: '东京' },
      { value: 'osaka', label: '大阪' },
      { value: 'kyoto', label: '京都' },
    ]
  }
]