import httpx
from fastapi import HTTPException
from app.config import settings

async def get_travel_recommendation(city: str, days: int, type: str) -> dict:
    prompt = f"你是一个专业旅行规划师，请为{type}类型的{days}天{city}旅行生成详细计划，包含每日景点、餐饮推荐、交通建议和预算分配。使用Markdown格式返回。"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat", # DeepSeek-V3 model
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": false
                }
            )
            
            result = response.json()
            if response.status_code != 200:
                print(f"API Error: {result}")
                raise HTTPException(status_code=500, detail="DeepSeek API 调用失败")
            
            # 获取 API 返回的 Markdown 内容
            markdown_content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Format the response to match database schema
            return {
                "content": markdown_content,
                "metadata": {
                    "city": city,
                    "days": days,
                    "type": type,
                    "format": "markdown",
                    "generated_at": datetime.now().isoformat()
                }
            }
            
        except Exception as e:
            print(f"Error: {str(e)}")
            raise HTTPException(status_code=500, detail="调用 DeepSeek API 时发生错误")