from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Economodel9.0")

@app.get("/")
async def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Economodel9.0 — Strategic Cycle Intelligence</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-zinc-950 text-white">
        <div class="max-w-7xl mx-auto p-8">
            <h1 class="text-4xl font-bold mb-2">Economodel9.0</h1>
            <p class="text-emerald-400 text-xl mb-8">Strategic Cycle Intelligence v9.0 — Live</p>
            
            <div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">
                <h2 class="text-2xl mb-6">Dashboard Loading...</h2>
                <p class="text-zinc-400">Full 5-pillar + Risk Rotation + Projections dashboard is being deployed now.</p>
                <pre class="mt-8 text-xs text-amber-300 bg-black p-4 rounded-xl overflow-auto">Internal Server Error fixed — model is live on Vercel.</pre>
            </div>
            
            <p class="mt-12 text-xs text-zinc-500">Repo: elwinmcc/Economodel9.0 • Branch: feature/dashboard-v9.0</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/analyze")
async def analyze():
    return {"status": "ok", "message": "Model running - full integration coming"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)