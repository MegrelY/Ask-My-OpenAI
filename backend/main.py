from fastapi import FastAPI
from .api import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Ask My OpenAI",
    description="API for querying OpenAI GPT-4",
    version="1.0.0"
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
