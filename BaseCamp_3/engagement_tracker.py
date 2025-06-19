from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# In-memory store for engagement data (replace with database in production)
engagement_data = []

@app.post("/track/engagement")
async def track_engagement(page: str, duration: float):
    entry = {"page": page, "duration": duration, "timestamp": datetime.now().isoformat()}
    engagement_data.append(entry)
    return JSONResponse(content={"status": "tracked", "count": len(engagement_data)})

@app.get("/engagement/stats")
async def get_engagement_stats():
    total_duration = sum(entry["duration"] for entry in engagement_data)
    return JSONResponse(content={"total_visits": len(engagement_data), "total_duration": total_duration})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)