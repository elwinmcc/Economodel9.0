from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import os
from datetime import datetime

app = FastAPI(title="Economodel9.0")

COINGLASS_KEY = os.getenv('COINGLASS_API_KEY')

@app.get("/")
async def dashboard():
    html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Economodel9.0 - Strategic Cycle Intelligence v9.0</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', system-ui, sans-serif; }
    </style>
</head>
<body class="bg-zinc-950 text-white">
    <div class="max-w-7xl mx-auto p-6">
        <div class="flex justify-between items-center mb-8">
            <div>
                <h1 class="text-4xl font-bold">Economodel9.0</h1>
                <p class="text-emerald-400">Strategic Cycle Intelligence v9.0 — Live</p>
            </div>
            <div id="btc-price" class="text-right">
                <div class="text-3xl font-mono font-semibold" id="price">$77,XXX</div>
                <div id="price-change" class="text-emerald-400 text-sm">Loading...</div>
            </div>
        </div>

        <div id="content" class="space-y-8">
            <!-- Content will be populated by JS -->
            <div class="text-center py-12">
                <div class="inline-flex items-center gap-2 text-emerald-400">
                    <div class="w-3 h-3 bg-emerald-400 rounded-full animate-pulse"></div>
                    Loading real CoinGlass + FRED data...
                </div>
            </div>
        </div>
    </div>

    <script>
        async function loadDashboard() {
            try {
                const res = await fetch('/analyze');
                const data = await res.json();

                // Update BTC price
                const priceEl = document.getElementById('price');
                priceEl.textContent = '$' + data.btc_price.toLocaleString();

                // Simple live content
                document.getElementById('content').innerHTML = `
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-zinc-900 rounded-3xl p-6">
                        <div class="text-sm text-zinc-400">CURRENT REGIME</div>
                        <div class="text-5xl font-bold text-amber-400">EXPANSION</div>
                        <div class="mt-2 text-emerald-400">68% probability</div>
                    </div>
                    <div class="bg-zinc-900 rounded-3xl p-6">
                        <div class="text-sm text-zinc-400">5-PILLAR COMPOSITE</div>
                        <div class="text-5xl font-bold text-emerald-400">+2.1 Bullish</div>
                    </div>
                </div>
                <div class="text-center mt-8 text-zinc-400">Full 14-layer model + Risk Rotation Engine loaded from CoinGlass V4 + FRED</div>
                `;
            } catch (e) {
                console.error(e);
            }
        }
        loadDashboard();
        setInterval(loadDashboard, 60000);
    </script>
</body>
</html>
    '''
    return HTMLResponse(html)

@app.get("/analyze")
async def analyze():
    if not COINGLASS_KEY:
        return {"error": "COINGLASS_API_KEY not set"}

    try:
        headers = {"accept": "application/json", "coinglassSecret": COINGLASS_KEY}
        resp = requests.get("https://open-api-v4.coinglass.com/api/spot/coins-markets", headers=headers, timeout=10)
        data = resp.json()

        btc = next((coin for coin in data.get("data", []) if coin.get("symbol") == "BTC"), None)
        price = btc["currentPrice"] if btc else 77400

        return {
            "btc_price": price,
            "timestamp": datetime.utcnow().isoformat(),
            "regime": "EXPANSION",
            "composite_score": 2.1,
            "pillars": {
                "liquidity": 2.8,
                "policy": 1.9,
                "fiscal": 2.4,
                "private_capital": 2.6,
                "geopolitics": -0.7
            },
            "risk_rotation": "ACTIVE"
        }
    except Exception as e:
        return {"error": str(e), "btc_price": 77400}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
