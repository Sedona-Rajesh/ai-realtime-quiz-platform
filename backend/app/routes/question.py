from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.question import Question
from app.schemas.question import QuestionCreate

router = APIRouter(prefix="/question", tags=["Question"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_question(data: QuestionCreate, db: Session = Depends(get_db)):
    question = Question(
        question_text=data.question_text,
        option_a=data.option_a,
        option_b=data.option_b,
        option_c=data.option_c,
        option_d=data.option_d,
        correct_option=data.correct_option,
        quiz_id=data.quiz_id
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question
