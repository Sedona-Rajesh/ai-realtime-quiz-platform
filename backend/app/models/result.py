from sqlalchemy import Column, Integer, String
from app.database import Base

class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True, index=True)
    quiz_code = Column(String, index=True)
    user_id = Column(String, index=True)
    score = Column(Integer)
