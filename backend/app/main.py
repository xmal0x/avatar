from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.paths import BASE_DIR
from .adapters.ai.openai_provider import OpenAIProvider
from .services.profile_loader import read_pdf_text, read_text_file, build_system_prompt
from .services.chat_service import ChatService
from .api.routes.chat import router as chat_router 

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup() -> None:
    pdf_path = (BASE_DIR / settings.assets_pdf).resolve()
    summary_path = (BASE_DIR / settings.assets_summary).resolve()

    linkedin_text = read_pdf_text(pdf_path)
    summary_text = read_text_file(summary_path)
    system_prompt = build_system_prompt(settings.name, summary_text, linkedin_text)

    ai = OpenAIProvider(api_key=settings.openai_api_key, model=settings.openai_model)
    chat = ChatService(ai=ai, system_prompt=system_prompt, max_messages=settings.history_max)

    app.state.ai_provider = ai
    app.state.chat_service = chat

@app.get("/")
def root():
    return {"status": "ok", "name": settings.name}

app.include_router(chat_router, prefix="/api/v1")
