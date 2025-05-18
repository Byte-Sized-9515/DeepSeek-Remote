#!/bin/bash

echo "Starting Cloudflare tunnel..."
cloudflared tunnel --url localhost:8000 &
CLOUDFLARED_PID=$!

sleep 6

echo "Activate virtual environment..."
conda activate web-ai

echo "Starting FastAPI server with Uvicorn..."
uvicorn main:app --host 0.0.0.0 --port 8000

# When FastAPI server exits, kill cloudflared
kill $CLOUDFLARED_PID