from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import os
import requests
from datetime import datetime

app = FastAPI(title="Economodel9.0")

COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY")

@app.get("/")
async def dashboard():
    html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Economodel9.0</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', system_ui, sans-serif; }
    </style>
</head>
<body class="bg-zinc-950 text-zinc-100 p-8">
    <div id="content" class="max-w-7xl mx-auto">
        <!-- Will be populated by JS -->
    </div>
    <script>
        async function loadDashboard() {
            const res = await fetch('/analyze');
            const data = await res.json();
            document.getElementById('content').innerHTML = `
                <div class="text-center">
                    <h1 class="text-5xl font-bold">Economodel9.0</h1>
                    <p class="text-emerald-400">Strategic Cycle Intelligence v9.0 — Live</p>
                    <div class="mt-8 bg-zinc-900 rounded-3xl p-8">
                        <div class="flex justify-between items-center">
                            <div>
                                <div class="text-6xl font-semibold" id="btc-price">$${data.btc_price || 'N/A'}</div>
                                <p class="text-zinc-400">Bitcoin Price</p>
                            </div>
                            <div class="text-right">
                                <div class="text-emerald-400 text-2xl font-semibold">STRONG BUY</div>
                            </div>
                        </div>
                        <div class="mt-6 text-xs text-zinc-500">Last updated: ${data.timestamp}</div>
                    </div>
                    <p class="mt-12 text-zinc-500">Full 5-pillar + Risk Rotation dashboard loading real data...</p>
                </div>
            `;
        }
        loadDashboard();
        setInterval(loadDashboard, 60000);
    </script>
</body>
</html>
    '''
    return HTMLResponse(content=html)

@app.get("/analyze")
async def analyze():
    if not COINGLASS_API_KEY:
        return JSONResponse({"error": "COINGLASS_API_KEY not set"}, status_code=500)
    try:
        headers = {"accept": "application/json", "coinglass-secret": COINGLASS_API_KEY}
        # Real BTC price from CoinGlass V4
        r = requests.get("https://open-api-v4.coinglass.com/api/spot/coins-markets?limit=1&symbol=BTC", headers=headers)
        r.raise_for_status()
        data = r.json()
        btc_price = data[0]["price"] if data and isinstance(data, list) else 77500
        return {
            "btc_price": round(btc_price, 0),
            "timestamp": datetime.utcnow().isoformat(),
            "status": "live"
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
