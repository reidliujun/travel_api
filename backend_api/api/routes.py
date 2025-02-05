from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from db.database import get_db
from models.travel import TravelRecommendation, City
from services.ai import get_travel_recommendation, get_city_info
from config import settings

router = APIRouter()

@router.get("/{city_name}/advice")
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

    # 调用 AI API
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

@router.get("/{city_name}/info")
async def get_city_information(
    city_name: str,
    db: Session = Depends(get_db)
):
    # Convert city name to lowercase for consistency
    city_name = city_name.lower()
    
    # Check if city exists in database
    city = db.query(City).filter(City.name == city_name).first()
    
    if city and city.description:
        return {
            "content": city.description,
            "metadata": {
                "city": city,
                "format": "markdown",
                "generated_at": datetime.now().isoformat()
            }
        } 
    
    # Get city info from AI
    city_info = await get_city_info(city_name)
    
    if city:
        # Update existing city
        city.description = city_info["content"]
        city.updated_at = datetime.now()
    else:
        # Create new city
        city = City(
            name=city_name,
            description=city_info["content"]
        )
        db.add(city)
    
    db.commit()
    db.refresh(city)
    
    return {
            "content": city.description,
            "metadata": {
                "city": city,
                "format": "markdown",
                "generated_at": datetime.now().isoformat()
            }
        } 