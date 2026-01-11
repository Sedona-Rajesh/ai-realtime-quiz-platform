import { useState } from "react";

export default function JoinQuiz() {
  const [quizCode, setQuizCode] = useState("");
  const [userId, setUserId] = useState("");
  const [ws, setWs] = useState(null);

  const joinQuiz = () => {
    const socket = new WebSocket(
      `ws://127.0.0.1:8000/ws/${quizCode}/${userId}`
    );

    socket.onopen = () => {
      console.log("Student connected");
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("STUDENT RECEIVED:", data);
    };

    setWs(socket);
  };

  return (
    <div>
      <h2>Student Join</h2>
      <input
        placeholder="Quiz Code"
        value={quizCode}
        onChange={(e) => setQuizCode(e.target.value)}
      />
      <input
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <button onClick={joinQuiz}>Join Quiz</button>
    </div>
  );
}
