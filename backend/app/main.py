from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import quiz



app = FastAPI(title="AI Assisted Real-Time Quiz Platform")
app.include_router(quiz.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Quiz API is running"}
