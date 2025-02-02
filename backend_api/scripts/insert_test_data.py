from sqlalchemy import create_engine, text
from datetime import datetime
import json
from app.config import settings

# Create database connection
engine = create_engine(settings.DATABASE_URL)

# Sample test data
test_data = [
    {
        "city": "tokyo",
        "days": 3,
        "type": "luxury",
        "recommendation": {
            "itinerary": "Day 1: Visit Tsukiji Market, Luxury lunch at Sukiyabashi Jiro, Shopping in Ginza\nDay 2: Private tea ceremony, Visit teamLab Borderless, Dinner at Narisawa\nDay 3: Private tour of Senso-ji Temple, Shopping in Omotesando, Dinner at RyuGin",
            "metadata": {
                "city": "tokyo",
                "days": 3,
                "type": "luxury",
                "format": "markdown"
            }
        }
    },
    {
        "city": "paris",
        "days": 2,
        "type": "normal",
        "recommendation": {
            "itinerary": "Day 1: Visit Eiffel Tower, Notre-Dame Cathedral, Seine River cruise\nDay 2: Louvre Museum, Walk through Montmartre, Evening at Sacré-Cœur",
            "metadata": {
                "city": "paris",
                "days": 2,
                "type": "normal",
                "format": "markdown"
            }
        }
    },
    {
        "city": "barcelona",
        "days": 4,
        "type": "budget",
        "recommendation": {
            "itinerary": "Day 1: Free walking tour, Visit La Boqueria market\nDay 2: Park Güell (free entry before 8am), Beach day\nDay 3: Gothic Quarter exploration, Free museum day\nDay 4: Sagrada Familia (exterior), Picnic at Ciutadella Park",
            "metadata": {
                "city": "barcelona",
                "days": 4,
                "type": "budget",
                "format": "markdown"
            }
        }
    },
        {
        "city": "shanghai",
        "days": 2,
        "type": "luxury",
        "recommendation": {
            "itinerary": """# 上海2日奢华之旅计划

## 📅 Day 1：经典与现代的极致碰撞
### 🏨 住宿安排
| 酒店 | 房型 | 特色 |
|------|------|------|
| 上海宝格丽酒店 | 外滩景观套房 | 24小时管家服务，BVLGARI洗浴套装 |

### 🌆 行程安排
| 时间 | 项目 | 详情 | 预算 |
|------|------|------|------|
| 10:00 | 接机服务 | 劳斯莱斯幻影机场迎接 | ¥3,800 |
| 11:30 | 云端午餐 | 莱美露滋（Maison Lameloise）米其林三星 | ¥2,800/人 |
| 14:00 | 外滩源探秘 | 安缦养云私人导览+明代古宅下午茶 | ¥6,500 |
| 17:00 | 高定购物 | 恒隆广场VIP室私密购物体验 | 根据消费浮动 |
| 19:30 | 黄浦夜宴 | Ultraviolet主厨20道式分子料理 | ¥8,888/人 |
| 22:00 | 夜景体验 | 宝格丽酒店顶层酒吧私人包场 | ¥12,000 |

### 🚗 本日交通
| 车型 | 服务时长 | 费用 |
|------|----------|------|
| 劳斯莱斯幻影 | 10小时 | ¥9,600 |
| 奔驰V级商务车（备用） | 待命状态 | ¥2,400 |

---

## 📅 Day 2：艺术与科技的沉浸体验
### 🏨 住宿安排
| 酒店 | 房型 | 特色 |
|------|------|------|
| 养云安缦 | 明清古宅院落 | 私人温泉泡池，禅修课程 |

### 🎨 行程安排
| 时间 | 项目 | 详情 | 预算 |
|------|------|------|------|
| 09:00 | 艺术早餐 | 浦东美术馆VIP包场+云端早餐 | ¥5,200 |
| 11:00 | 科技体验 | 上海天文馆专属导览+穹顶影院 | ¥3,800 |
| 13:30 | 本帮盛宴 | 甬府（龙柏店）黄鱼宴定制菜单 | ¥4,600/人 |
| 16:00 | 私人收藏 | 西岸艺术中心藏家专场 | ¥18,000 |
| 18:30 | 浦江巡航 | Sunseeker 68游艇晚宴（含侍酒师） | ¥28,000 |
| 21:00 | 水疗体验 | 安缦SPA钻石护理疗程 | ¥6,800 |

### 🚁 特色交通
| 项目 | 说明 | 费用 |
|------|------|------|
| 直升机巡游 | 外滩-陆家嘴空中观光（15分钟） | ¥18,000 |
| 特斯拉Model X护航车队 | 艺术区专属接驳 | ¥4,200 |

---

## 💰 总预算明细
| 类别 | 明细项 | 金额 |
|------|--------|------|
| **住宿** | 宝格丽酒店1晚 + 养云安缦1晚 | ¥36,000 |
| **餐饮** | 3家米其林餐厅 + 游艇晚宴 | ¥46,796 |
| **交通** | 豪车接送 + 直升机体验 | ¥42,200 |
| **体验** | 私人导览 + SPA + 艺术专场 | ¥48,600 |
| **服务费** | 双语管家 + 安保团队 | ¥15,000 |
| **预备金** | 应急及额外消费 | ¥20,000 |
| **总计** | | **¥208,596** |

---

## ✨ 增值服务推荐
```markdown
| 服务项目 | 内容 | 费用 |
|----------|------|------|
| 私人摄影师 | 8K电影级旅拍（含后期制作） | ¥12,000/天 |
| 珠宝武装押运 | 贵重物品银行级安保运输 | ¥8,000/次 |
| 高定旗袍速裁 | 「瀚艺」48小时定制服务 | ¥35,000起 |
| 葡萄酒窖直送 | 康帝酒庄垂直年份精选 | 按酒款定价 |

> 💡 温馨提示：所有米其林餐厅需提前21天预定，直升机飞行需提前报备航线""",
            "metadata": {
                "city": "shanghai",
                "days": 2,
                "type": "luxury",
                "format": "markdown"
            }
        }
    }
]

# SQL query to insert data
insert_query = """
INSERT INTO travel_recommendations (city, days, type, recommendation, created_at, updated_at)
VALUES (
    :city,
    :days,
    :type,
    :recommendation::jsonb,
    :created_at,
    :updated_at
)
"""

# Execute insertions
# 修改执行部分
with engine.connect() as conn:
    for data in test_data:
        stmt = text("""
            INSERT INTO travel_recommendations (city, days, type, recommendation, created_at, updated_at)
            VALUES (:city, :days, :type, cast(:recommendation as jsonb), :created_at, :updated_at)
        """)
        
        conn.execute(
            stmt,
            {
                "city": data["city"],
                "days": data["days"],
                "type": data["type"],
                "recommendation": json.dumps(data["recommendation"]),
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
        )
        conn.commit()

print("Test data inserted successfully!")