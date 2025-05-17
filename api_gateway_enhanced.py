
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import logging
import uuid

# Configure centralized logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("logs/api_gateway.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI(
    title="Intent Field Actuator - Enhanced API Gateway",
    version="1.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for latency benchmarking and UUID tagging
@app.middleware("http")
async def latency_monitor(request: Request, call_next):
    event_id = str(uuid.uuid4())
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    response.headers["X-Event-ID"] = event_id

    if process_time > 0.2:
        logging.warning(f"[High Latency] {process_time:.4f}s on {request.url.path} | Event ID: {event_id}")
    else:
        logging.info(f"[Processed] {process_time:.4f}s on {request.url.path} | Event ID: {event_id}")
    
    return response

@app.get("/")
async def root():
    return {
        "message": "Guardian Code Final Validation Environment is Live",
        "version": "1.0.1",
        "status": "operational"
    }

@app.get("/status/latency")
async def latency_status():
    return {
        "message": "Latency benchmarking active",
        "threshold_sec": 0.2,
        "log_file": "logs/api_gateway.log"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_gateway_enhanced:app", host="0.0.0.0", port=8000, reload=True)
