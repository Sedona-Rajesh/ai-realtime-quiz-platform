import { useState } from "react";

export default function HostQuiz() {
  const [quizCode, setQuizCode] = useState("");
  const [ws, setWs] = useState(null);

  const connectHost = () => {
    const socket = new WebSocket(
      `ws://127.0.0.1:8000/ws/${quizCode}/host`
    );

    socket.onopen = () => {
      console.log("Host connected");
    };

    socket.onmessage = (event) => {
      console.log("HOST RECEIVED:", JSON.parse(event.data));
    };

    setWs(socket);
  };

  const startQuestion = () => {
    ws.send(
      JSON.stringify({
        type: "start_question",
        question_text: "Best case of linear search?",
        options: ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
        correct_answer: "O(1)",
        time: 10,
      })
    );
  };

  return (
    <div>
      <h2>Host</h2>
      <input
        placeholder="Quiz Code"
        value={quizCode}
        onChange={(e) => setQuizCode(e.target.value)}
      />
      <button onClick={connectHost}>Connect Host</button>
      <br />
      <button onClick={startQuestion}>Start Question</button>
    </div>
  );
}
