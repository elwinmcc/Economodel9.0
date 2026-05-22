from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import requests

app = FastAPI(title="Economodel9.0")

@app.get("/")
async def dashboard():
    return HTMLResponse("""
    <h1>Economodel9.0 - Live on Railway</h1>
    <p>Dashboard is loading with real CoinGlass data...</p>
    """)

@app.get("/analyze")
async def analyze():
    try:
        api_key = os.getenv("COINGLASS_API_KEY")
        if not api_key:
            return {"error": "No COINGLASS_API_KEY"}
        
        headers = {"accept": "application/json", "coinglassSecret": api_key}
        response = requests.get("https://open-api-v4.coinglass.com/api/spot/coins-markets", headers=headers, timeout=10)
        data = response.json()
        btc_price = data.get("data", [{}])[0].get("currentPrice") if data.get("data") else None
        
        return {
            "btc_price": btc_price,
            "status": "live",
            "timestamp": "now"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
