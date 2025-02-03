import httpx
from datetime import datetime
from fastapi import HTTPException
from config import settings

async def get_travel_recommendation(city: str, days: int, type: str) -> dict:
    prompt = f"你是一个专业旅行规划师，请为{type}类型的{days}天{city}旅行生成详细计划，包含每日景点、餐饮推荐、交通建议和预算分配。使用包含表格的Markdown格式返回。控制字数在300字以内。"
    
    async with httpx.AsyncClient(timeout=1000.0) as client:  # Set timeout to 5 minutes
        try:
            headers = {
                "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }
            body = {
                "model": "deepseek-ai/DeepSeek-V3",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = await client.post(
                "https://api.siliconflow.cn/v1/chat/completions",
                headers=headers,
                json=body
            )
            
            if response.status_code == 409:
                raise HTTPException(status_code=429, detail="API 调用频率超限，请稍后重试")
            elif response.status_code == 503:
                raise HTTPException(status_code=503, detail="模型服务过载，请稍后重试")
            elif response.status_code != 200:
                print(f"API Error: {response.text}")
                raise HTTPException(status_code=500, detail="DeepSeek API 调用失败")
            
            # 获取 API 返回的 Markdown 内容
            result = response.json()
            markdown_content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Format the response to match database schema
            return {
                "itinerary": markdown_content,
                "metadata": {
                    "city": city,
                    "days": days,
                    "type": type,
                    "format": "markdown",
                    "generated_at": datetime.now().isoformat()
                }
            }
            
        except HTTPException:
            raise
        except Exception as e:
            print(f"Error: {str(e)}")
            raise HTTPException(status_code=500, detail="调用 DeepSeek API 时发生错误")