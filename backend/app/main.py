from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import quiz
from app.routes import ws

from app.routes import question


app = FastAPI(title="AI Assisted Real-Time Quiz Platform")
app.include_router(quiz.router)
app.include_router(question.router)
app.include_router(ws.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Quiz API is running"}
