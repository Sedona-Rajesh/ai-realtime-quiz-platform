# AI-Assisted Real-Time Quiz Platform (MVP)

An intelligent real-time quiz platform that combines **live assessments**, **AI-assisted question generation**, **explanation-based feedback**, and **lightweight anti-cheating** to improve both evaluation quality and learning outcomes.

This project is designed as a **resume-grade individual project**, focusing on clean system design, real-time communication, and responsible AI integration.

---

## 🚀 Key Features (MVP)

### 🔴 Real-Time Quiz System
- Live quiz sessions using WebSockets
- Host & participant roles
- Join quiz using a unique quiz code
- Timed questions with automatic locking
- Live leaderboard and score updates

### 🤖 AI-Assisted Question Generation
- Generate MCQs from uploaded source material (text / short PDF)
- Host can:
  - Highlight important topics
  - Provide example questions
- AI generates remaining questions following the given pattern
- Human-in-the-loop review before publishing

### 📚 Explanation-Based Feedback
- Students receive:
  - Correct / Incorrect status
  - AI-generated explanation for each answer
- Focuses on *why* an answer is right or wrong

### 🔐 Lightweight Anti-Cheating
- Tab switch detection
- Abnormal response-time logging
- Attempts flagged as **Normal / Suspicious**
- Privacy-aware (no webcam or screen recording)

---

## 🧠 Why This Project?

Most existing quiz platforms focus on **engagement and scores**, but provide:
- Limited learning feedback
- Manual quiz creation overhead
- Weak assessment integrity in remote settings

This project addresses those gaps by:
- Assisting hosts with AI-driven content creation
- Providing explanation-based learning feedback
- Maintaining fairness using behavior-based anti-cheating
- Supporting live, synchronous assessments

---

## 🛠 Tech Stack

### Backend
- **FastAPI (Python)**
- REST APIs + WebSockets
- SQLAlchemy ORM

### Database
- SQLite (MVP)
- Designed to be portable to PostgreSQL / MySQL

### Frontend 
- React
- WebSocket client for real-time updates

### AI Integration
- LLM API (prompt-engineered)
- Few-shot, example-guided generation
- Structured JSON outputs

---

## 🧩 System Architecture (High-Level)

Client (React)
↕ WebSocket / HTTP
FastAPI Backend
↕
Database (Quiz, Questions, Responses)
↕
AI Service (Question & Explanation Generation)


---

## 📂 Project Structure

quiz-app/
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── database.py # DB configuration
│ │ ├── models/ # SQLAlchemy models
│ │ ├── schemas/ # Pydantic schemas
│ │ ├── routes/ # API routes
│ └── requirements.txt
├── .gitignore
└── README.md

