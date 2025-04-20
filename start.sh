#!/bin/bash

echo "Starting Cloudflare tunnel..."
cloudflared tunnel --url localhost:1194 &
CLOUDFLARED_PID=$!

sleep 6

echo "Activate virtual environment..."
source venv/bin/activate

echo "Starting Flask server..."
python3 server.py

# When Flask server exits, kill cloudflared
kill $CLOUDFLARED_PID