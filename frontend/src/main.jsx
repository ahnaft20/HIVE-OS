import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

import { AgentProvider } from "./context/AgentContext";
import { TimelineProvider } from "./context/TimelineContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <TimelineProvider>
      <AgentProvider>
        <App />
      </AgentProvider>
    </TimelineProvider>
  </React.StrictMode>
);