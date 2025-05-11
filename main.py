from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/collect")
async def collect_info(request: Request):
    data = await request.json()
    ip = request.client.host
    print("Received device info from:", ip)
    print(data)
    return {"status": "received", "ip": ip}
