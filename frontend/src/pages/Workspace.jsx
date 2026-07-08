import { useState, useContext } from "react";
import { sendMessage } from "../services/api";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";
import { AgentContext } from "../context/AgentContext";

export default function Workspace() {
  const {
    messages,
    setMessages,
    agents,
    setAgents
  } = useContext(AgentContext);

  const [loading, setLoading] = useState(false);

  async function handleSend(text) {
    if (!text.trim()) return;

    const userMessage = {
      role: "user",
      content: text
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    // Research starts
    setAgents((prev) => ({
      ...prev,
      research: "thinking"
    }));

    try {
      const res = await sendMessage(text);

      setAgents({
        research: "done",
        engineer: "done",
        designer: "done",
        leader: "done",
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: res.reply,
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Backend connection failed.",
        },
      ]);
    }

    setLoading(false);
  }

  return (
    <>
      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput
        onSend={handleSend}
      />
    </>
  );
}