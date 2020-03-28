import React from "react";
import logo from "./chef.png";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Cooooooooooook</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          And Boooooooook
        </a>
      </header>
    </div>
  );
}

export default App;
