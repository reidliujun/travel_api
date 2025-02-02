from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.db.database import get_db
from app.models.travel import TravelRecommendation
from app.services.deepseek import get_travel_recommendation
from app.config import settings

router = APIRouter()

@router.get("/{city_name}")
async def get_travel_advice(
    city_name: str,
    days: int,
    type: str,
    db: Session = Depends(get_db)
):
    # 将城市名和类型转换为小写
    city_name = city_name.lower()
    type = type.lower()
    
    if days < 1 or days > 7:
        raise HTTPException(status_code=400, detail="天数必须在1到7之间")
    
    if type not in ["luxury", "normal", "budget"]:
        raise HTTPException(status_code=400, detail="类型必须是 luxury、normal 或 budget")

    # 检查缓存
    cache = db.query(TravelRecommendation).filter(
        TravelRecommendation.city == city_name,
        TravelRecommendation.days == days,
        TravelRecommendation.type == type
    ).first()

    # 如果缓存存在且未过期
    if cache and (datetime.now() - cache.updated_at).days < settings.CACHE_EXPIRY_DAYS:
        return cache.recommendation

    # 调用 DeepSeek API
    recommendation = await get_travel_recommendation(city_name, days, type)

    if cache:
        # 更新现有记录
        cache.recommendation = recommendation
        cache.updated_at = datetime.now()
    else:
        # 创建新记录
        cache = TravelRecommendation(
            city=city_name,
            days=days,
            type=type,
            recommendation=recommendation
        )
        db.add(cache)

    db.commit()
    return recommendation