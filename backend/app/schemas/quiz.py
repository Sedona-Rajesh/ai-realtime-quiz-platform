from pydantic import BaseModel

class QuizCreate(BaseModel):
    title: str
    description: str | None = None

class QuizResponse(QuizCreate):
    id: int
    quiz_code: str

    class Config:
        orm_mode = True
