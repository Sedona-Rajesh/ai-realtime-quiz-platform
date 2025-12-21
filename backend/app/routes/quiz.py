import random
import string
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database import SessionLocal
from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate

router = APIRouter(prefix="/quiz", tags=["Quiz"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_quiz(data: QuizCreate, db: Session = Depends(get_db)):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    quiz = Quiz(
        title=data.title,
        description=data.description,
        quiz_code=code
    )
    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    return quiz

@router.get("/join/{quiz_code}")
def join_quiz(quiz_code: str, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.quiz_code == quiz_code).first()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {
        "message": "Joined quiz successfully",
        "quiz_id": quiz.id,
        "title": quiz.title,
        "description": quiz.description
    }