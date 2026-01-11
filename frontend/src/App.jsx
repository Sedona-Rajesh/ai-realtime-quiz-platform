import JoinQuiz from "./components/JoinQuiz";
import HostQuiz from "./components/HostQuiz";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Realtime Quiz App</h1>
      <JoinQuiz />
      <hr />
      <HostQuiz />
    </div>
  );
}

export default App;
