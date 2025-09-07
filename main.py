from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from model import model

app = FastAPI()


app.mount("/static", StaticFiles(directory="static", html=True), name="static")


def gemini_ai(prompt):
    prompt = prompt
    response = model.generate_content(contents=[prompt])
    return response.text


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_home():
    return FileResponse("static/chat.html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("message", "")
    response = model.generate_content(contents=[prompt])
    return JSONResponse(content={"response": f"Gemini: {response}"})
