import { createContext, useContext, useState } from "react";

const AgentContext = createContext();

export function AgentProvider({ children }) {
  const [agents, setAgents] = useState({
    research: {
      name: "Research",
      role: "Research Specialist",
      icon: "🧠",
      status: "Ready",
      output: "",
      confidence: 95,
    },
    engineer: {
      name: "Engineer",
      role: "Software Engineer",
      icon: "💻",
      status: "Ready",
      output: "",
      confidence: 95,
    },
    designer: {
      name: "Designer",
      role: "UI/UX Designer",
      icon: "🎨",
      status: "Ready",
      output: "",
      confidence: 95,
    },
    documentation: {
      name: "Documentation",
      role: "Technical Writer",
      icon: "📄",
      status: "Ready",
      output: "",
      confidence: 95,
    },
    leader: {
      name: "Leader",
      role: "Chief Executive Officer",
      icon: "👑",
      status: "Ready",
      output: "",
      confidence: 95,
    },
    qa: {
      name: "QA",
      role: "Quality Assurance",
      icon: "🧪",
      status: "Ready",
      output: "",
      confidence: 95,
    },
  });

  function updateAgent(name, status, output = "") {
    setAgents((prev) => ({
      ...prev,
      [name]: {
        ...prev[name],
        status,
        output,
      },
    }));
  }

  function resetAgents() {
    setAgents({
      research: {
        name: "Research",
        role: "Research Specialist",
        icon: "🧠",
        status: "Ready",
        output: "",
        confidence: 95,
      },
      engineer: {
        name: "Engineer",
        role: "Software Engineer",
        icon: "💻",
        status: "Ready",
        output: "",
        confidence: 95,
      },
      designer: {
        name: "Designer",
        role: "UI/UX Designer",
        icon: "🎨",
        status: "Ready",
        output: "",
        confidence: 95,
      },
      documentation: {
        name: "Documentation",
        role: "Technical Writer",
        icon: "📄",
        status: "Ready",
        output: "",
        confidence: 95,
      },
      leader: {
        name: "Leader",
        role: "Chief Executive Officer",
        icon: "👑",
        status: "Ready",
        output: "",
        confidence: 95,
      },
      qa: {
        name: "QA",
        role: "Quality Assurance",
        icon: "🧪",
        status: "Ready",
        output: "",
        confidence: 95,
      },
    });
  }

  return (
    <AgentContext.Provider
      value={{
        agents,
        updateAgent,
        resetAgents,
      }}
    >
      {children}
    </AgentContext.Provider>
  );
}

export function useAgents() {
  return useContext(AgentContext);
}