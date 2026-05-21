from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Economodel9.0")

@app.get("/")
async def dashboard():
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Economodel9.0 — Strategic Cycle Intelligence v9.0</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', system_ui, sans-serif; }
        .card { transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); }
        .card:hover { transform: translateY(-2px); box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); }
    </style>
</head>
<body class="bg-zinc-950 text-zinc-100">
    <div class="max-w-7xl mx-auto p-6">
        <!-- Header -->
        <div class="flex items-center justify-between mb-8">
            <div>
                <h1 class="text-4xl font-semibold tracking-tighter">Economodel9.0</h1>
                <p class="text-emerald-400 text-lg">Strategic Cycle Intelligence v9.0 — Live</p>
            </div>
            <div class="flex items-center gap-4">
                <div class="bg-zinc-900 px-4 py-2 rounded-2xl flex items-center gap-2">
                    <div class="w-3 h-3 bg-emerald-400 rounded-full animate-pulse"></div>
                    <span class="text-sm font-medium">BTC $94,820</span>
                </div>
                <div class="px-6 py-2 bg-emerald-500/10 text-emerald-400 rounded-3xl text-sm font-semibold flex items-center gap-1.5">
                    <span>STRONG BUY</span>
                    <span class="text-xs bg-emerald-400 text-zinc-950 px-2 py-0.5 rounded-2xl">+2.4%</span>
                </div>
            </div>
        </div>

        <!-- Regime + Signal -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="bg-zinc-900 rounded-3xl p-6">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="text-zinc-400 text-sm">CURRENT REGIME</p>
                        <p class="text-3xl font-semibold text-amber-400">EXPANSION</p>
                    </div>
                    <div class="text-right">
                        <div class="inline-flex items-center px-4 py-1 bg-amber-400/10 text-amber-400 rounded-2xl text-sm font-medium">68% probability</div>
                    </div>
                </div>
                <div class="mt-6 h-2 bg-zinc-800 rounded-3xl overflow-hidden">
                    <div class="h-full w-3/4 bg-gradient-to-r from-amber-400 to-yellow-400"></div>
                </div>
            </div>

            <div class="bg-zinc-900 rounded-3xl p-6 col-span-2">
                <p class="text-zinc-400 text-sm mb-3">5-PILLAR COMPOSITE SCORE</p>
                <div class="flex items-baseline gap-3">
                    <span class="text-7xl font-semibold tracking-tighter">+2.1</span>
                    <span class="text-emerald-400 text-2xl">Bullish</span>
                </div>
                <p class="text-zinc-400 text-sm">Risk Rotation Active • Warsh Policy Neutral</p>
            </div>
        </div>

        <!-- 5 Pillars -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-4 mb-8">
            <div class="bg-zinc-900 rounded-3xl p-5 card">
                <p class="text-xs text-zinc-400">LIQUIDITY</p>
                <p class="text-4xl font-semibold text-emerald-400">+2.8</p>
                <p class="text-xs text-emerald-400">Net Liquidity ↑</p>
            </div>
            <div class="bg-zinc-900 rounded-3xl p-5 card">
                <p class="text-xs text-zinc-400">POLICY / WARSH</p>
                <p class="text-4xl font-semibold text-emerald-400">+1.9</p>
                <p class="text-xs text-amber-400">Discipline Active</p>
            </div>
            <div class="bg-zinc-900 rounded-3xl p-5 card">
                <p class="text-xs text-zinc-400">FISCAL / STABLECOINS</p>
                <p class="text-4xl font-semibold text-emerald-400">+2.4</p>
                <p class="text-xs text-emerald-400">Flywheel Accelerating</p>
            </div>
            <div class="bg-zinc-900 rounded-3xl p-5 card">
                <p class="text-xs text-zinc-400">PRIVATE CAPITAL / ETF</p>
                <p class="text-4xl font-semibold text-emerald-400">+2.6</p>
                <p class="text-xs text-emerald-400">Institutional Inflows</p>
            </div>
            <div class="bg-zinc-900 rounded-3xl p-5 card">
                <p class="text-xs text-zinc-400">GEOPOLITICS / OIL</p>
                <p class="text-4xl font-semibold text-amber-400">-0.7</p>
                <p class="text-xs text-amber-400">Oil Headwind</p>
            </div>
        </div>

        <!-- Risk Rotation -->
        <div class="bg-zinc-900 rounded-3xl p-6 mb-8">
            <h2 class="text-lg font-semibold mb-4">Risk Rotation Engine</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="bg-zinc-800 rounded-2xl p-4">
                    <div class="flex justify-between">
                        <span class="text-sm">Stables → BTC</span>
                        <span class="text-emerald-400 font-medium">VERY STRONG</span>
                    </div>
                    <div class="h-2 bg-emerald-400 rounded mt-3"></div>
                </div>
                <div class="bg-zinc-800 rounded-2xl p-4">
                    <div class="flex justify-between">
                        <span class="text-sm">BTC → ETH</span>
                        <span class="text-emerald-400 font-medium">STRONG</span>
                    </div>
                    <div class="h-2 bg-emerald-400 rounded mt-3 w-4/5"></div>
                </div>
                <div class="bg-zinc-800 rounded-2xl p-4">
                    <div class="flex justify-between">
                        <span class="text-sm">ETH → Alts</span>
                        <span class="text-amber-400 font-medium">FORMING</span>
                    </div>
                    <div class="h-2 bg-amber-400 rounded mt-3 w-1/2"></div>
                </div>
                <div class="bg-zinc-800 rounded-2xl p-4">
                    <div class="flex justify-between">
                        <span class="text-sm">Macro → Crypto</span>
                        <span class="text-emerald-400 font-medium">ACTIVE</span>
                    </div>
                    <div class="h-2 bg-emerald-400 rounded mt-3 w-11/12"></div>
                </div>
            </div>
        </div>

        <!-- Projections -->
        <div class="bg-zinc-900 rounded-3xl p-6">
            <h2 class="text-lg font-semibold mb-4">Projections (Regime-Adjusted)</h2>
            <table class="w-full">
                <thead>
                    <tr class="border-b border-zinc-700">
                        <th class="text-left py-3 text-zinc-400 text-sm">Horizon</th>
                        <th class="text-right py-3 text-zinc-400 text-sm">Bear</th>
                        <th class="text-right py-3 text-zinc-400 text-sm">Base</th>
                        <th class="text-right py-3 text-zinc-400 text-sm">Bull</th>
                        <th class="text-right py-3 text-zinc-400 text-sm">P5–P95</th>
                    </tr>
                </thead>
                <tbody class="text-sm">
                    <tr class="border-b border-zinc-700">
                        <td class="py-4">90 days</td>
                        <td class="text-right text-red-400">$81k</td>
                        <td class="text-right font-medium">$108k</td>
                        <td class="text-right text-emerald-400">$132k</td>
                        <td class="text-right text-zinc-400">$79k – $141k</td>
                    </tr>
                    <tr class="border-b border-zinc-700">
                        <td class="py-4">180 days</td>
                        <td class="text-right text-red-400">$92k</td>
                        <td class="text-right font-medium">$142k</td>
                        <td class="text-right text-emerald-400">$178k</td>
                        <td class="text-right text-zinc-400">$87k – $192k</td>
                    </tr>
                    <tr>
                        <td class="py-4">365 days</td>
                        <td class="text-right text-red-400">$118k</td>
                        <td class="text-right font-medium">$214k</td>
                        <td class="text-right text-emerald-400">$287k</td>
                        <td class="text-right text-zinc-400">$104k – $312k</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="text-center text-zinc-500 text-xs mt-12">
            Economodel9.0 • 5-Pillar + Risk Rotation Framework • Live on Vercel • May 21, 2026
        </div>
    </div>
</body>
</html>
    '''
    return HTMLResponse(content=html)

@app.get("/analyze")
async def analyze():
    return {"status": "ok", "message": "Full model ready for integration"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
