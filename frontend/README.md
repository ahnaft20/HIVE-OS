# 🐝 HIVE OS

> Autonomous Multi-Agent AI Software Engineering Platform

HIVE OS is an AI-powered multi-agent operating system that simulates a real software company. Instead of relying on a single AI assistant, HIVE OS assigns specialized AI agents to different responsibilities, allowing them to collaborate and produce a complete software development plan.

Built for the **AMD Developer Hackathon Act II**.

---

# ✨ Features

- 🧠 Research Agent
- 💻 Engineering Agent
- 🎨 UI/UX Design Agent
- 📄 Documentation Agent
- 🧪 QA Agent
- 👑 CEO Agent (Executive Decision Maker)

Additional capabilities:

- Live Agent Dashboard
- Workflow Visualization
- Activity Timeline
- Project Generator
- File Explorer
- Terminal Logs
- Dynamic Resource Dashboard
- Recovery System
- Memory System
- Modular Architecture

---

# 🏗️ Architecture

```
                User Prompt
                     │
                     ▼
             ┌────────────────┐
             │   CEO / Leader │
             └────────────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Research      Engineering      Design
      │              │              │
      └───────┬──────┴───────┬──────┘
              ▼              ▼
       Documentation        QA
              │
              ▼
        Executive Decision
```

---

# 🚀 Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS
- Lucide Icons

### Backend

- FastAPI
- Python
- Ollama

### AI

- Llama 3.2
- Multi-Agent Architecture

---

# 📂 Project Structure

```
frontend/
backend/
generated_projects/
agents/
core/
```

---

# ⚙️ Installation

## Backend

```bash
cd backend

venv\Scripts\activate

uvicorn main:app --reload
```

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🧩 Multi-Agent Workflow

1. User submits a prompt.
2. Research analyzes the problem.
3. Engineering designs the technical solution.
4. Design creates the UI/UX strategy.
5. Documentation prepares the implementation roadmap.
6. QA reviews the complete solution.
7. CEO evaluates every department and makes the final executive decision.

---

# 📸 Screenshots

Add screenshots here before submission.

- Dashboard
- Workflow Graph
- Final Report
- Agent Collaboration

---

# 🎯 Future Roadmap

- Larger language models
- Cloud inference
- Real code generation
- Plugin marketplace
- Multi-model routing
- Team collaboration

---

# 📜 License

MIT License

---

Built with ❤️ for the AMD Developer Hackathon Act II.