import random
import string
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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
