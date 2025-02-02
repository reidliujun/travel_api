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
                "city": "Tokyo",
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
                "city": "Paris",
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
                "city": "Barcelona",
                "days": 4,
                "type": "budget",
                "format": "markdown"
            }
        }
    },
        {
        "city": "shanghai",
        "days": 3,
        "type": "luxury",
        "recommendation": {
            "itinerary": """# 上海3日奢华之旅计划
## 📅 Day 1：经典地标与浦江夜色
### 🏛️ 景点安排
- **上午**  
  10:00 半岛酒店私人礼宾车接机  
  11:00 入住 **上海宝格丽酒店**（外滩景观套房）  
- **下午**  
  14:00 **豫园安缦·养云** 私人导览（含明代古宅下午茶）  
  16:30 **外滩源壹号** 历史建筑探秘（原英国领事馆）  
- **晚间**  
  19:00 **Jean-Georges** 米其林三星法餐（陆家嘴店）  
  21:00 **BFC外滩游艇会** 私人游艇夜游黄浦江

### 🚗 交通方案
- 全程 **梅赛德斯-迈巴赫S680** 专属接送  
- 黄浦江游艇使用 **Sunseeker Manhattan 66** 型号

### 💰 本日预算
| 项目 | 金额 |
|------|------|
| 住宿 | ¥8,800 |
| 餐饮 | ¥5,200 |
| 交通 | ¥6,500 |
| 体验 | ¥12,000 |
| **小计** | **¥32,500** |

---

## 📅 Day 2：摩登艺术与云端体验
### 🎨 景点安排
- **上午**  
  09:30 **上海中心大厦** VIP通道登顶（含云端早餐）  
  11:30 **浦东美术馆** 包场参观（含策展人讲解）  
- **下午**  
  14:00 **镛舍酒店·随堂里** 创意本帮菜私宴  
  16:00 **西岸艺术中心** 私人藏家展厅开放  
- **晚间**  
  19:30 **Ultraviolet by Paul Pairet** 沉浸式分子料理（20道式主厨菜单）  
  22:00 **Flair Rooftop** 丽思卡尔顿顶层酒吧观景

### 🚁 特色交通
- 下午艺术巡礼使用 **宾利添越** 艺术主题定制车
- 可选 **直升机巡游** 加价体验（¥28,000/30分钟）

### 💰 本日预算
| 项目 | 金额 |
|------|------|
| 住宿 | ¥8,800 |
| 餐饮 | ¥9,800 |
| 交通 | ¥9,200 |
| 体验 | ¥18,000 |
| **小计** | **¥45,800** |

---

## 📅 Day 3：隐秘奢华与定制收藏
### 🛍️ 景点安排
- **上午**  
  09:00 **思南公馆** 古董珠宝私洽会  
  11:00 **衡山路-东平路** 设计师品牌高定体验  
- **下午**  
  13:00 **建业里嘉佩乐** 石库门别墅私房菜  
  15:00 **龙美术馆** 私人导览+艺术品收藏咨询  
  17:00 **宝格丽酒店** 水疗中心钻石护理疗程

### 🍽️ 餐饮亮点
- 午餐体验 **甬府尊鲜** 黄鱼宴（需提前3日预定野生大黄鱼）
- 下午茶 **Salon de Thé de Joël Robuchon** 鱼子酱主题套餐

### 💰 本日预算
| 项目 | 金额 |
|------|------|
| 住宿 | ¥8,800 |
| 餐饮 | ¥7,600 |
| 购物 | ¥50,000+ |
| 体验 | ¥25,000 |
| **小计** | **¥91,400+** |

---

## 💎 总预算概览
| 类别 | 金额 |
|------|------|
| **基础消费** | ¥169,700 |
| **可选升级项** | ¥80,000+ |
| **建议预备金** | ¥50,000 |
| **总计** | ¥300,000± |

---

## ✨ 增值服务推荐
1. **私人影像团队**（8K电影级旅拍 ¥18,000/天）
2. **外滩源私人管家**（历史学家随行讲解 ¥6,800/半天）
3. **高定旗袍速裁**（「蔓楼兰」48小时定制 ¥28,000起）
4. **珠宝保险箱配送**（四大行武装押运服务）

> 💡 贴士：所有米其林餐厅需提前14天预定，私密行程建议通过 **Quintessentially** 等顶级礼宾公司安排""",
            "metadata": {
                "city": "Barcelona",
                "days": 4,
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