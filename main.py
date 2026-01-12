from students import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# If you have routers, import them like this
# from app.routes import morse
# from app.database import engine
# from app.models import Base

app = FastAPI(
    title="CRUD API",
    description="CRUD API for Hackathon",
    version="1.0.0",
)

# CORS (safe default for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables (ONLY if you're using SQLAlchemy)
# Base.metadata.create_all(bind=engine)

# Register routes
# app.include_router(morse.router, prefix="/morse", tags=["Morse"])


@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(router)
