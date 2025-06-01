import logging
import json
import asyncio
from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from user_agents import parse # pip install pyyaml ua-parser user-agents
import ollama

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.get("/")
async def serve_correct_interface(request: Request, user_agent: str = Header(None)):
    try:
        ua = parse(user_agent or "")
        template = "chat-mobile.html" if ua.is_mobile else "chat.html"
        return templates.TemplateResponse(template, {"request": request})
    except Exception as e:
        # Fallback to desktop if detection fails
        logging.error(f"User agent parsing failed: {str(e)}")
        return templates.TemplateResponse("chat.html", {"request": request})

# Handle the POST request to process the chat with streaming
@app.post("/process")
async def process(request: Request):
    data = await request.json()
    prompt = data['prompt']
    mode = data.get('mode', 'chat')

    async def generate():
        try:
            # Get the sync generator first
            sync_generator = ollama.chat(
                model='deepseek-r1:14b',
                messages=[{
                    "role": "user",
                    "content": f"{mode} mode: {prompt}"
                }],
                stream=True
            )
            
            # Convert sync generator to async
            for chunk in sync_generator:
                yield f"data: {json.dumps({'response': chunk['message']['content']})}\n\n"
                await asyncio.sleep(0)  # Yield control to event loop
                
        except Exception as e:
            logging.error(f"Streaming error: {str(e)}")
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")

# Optional: Keep refresh endpoint if you want to implement some cleanup
@app.post("/refresh")
async def refresh():
    # This endpoint could be used for any necessary cleanup
    logging.debug("Refresh request received")
    return JSONResponse(content={"response": "Server refreshed."})