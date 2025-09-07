from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from views import get_gpt_answer, get_gemini_answer

app = FastAPI()


app.mount(
    "/static", StaticFiles(directory="static", html=True),
    name="static"
)


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
    response_1 = get_gemini_answer(prompt)
    response_2 = get_gpt_answer(prompt)
    return JSONResponse(content={
        "response": f"{response_1} {response_2}"
    })
