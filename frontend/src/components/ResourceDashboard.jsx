import {
  Cpu,
  Brain,
  Clock3,
  Database,
  Server,
  Target,
} from "lucide-react";

export default function ResourceDashboard({
  activeAgents = 0,
  model = "llama3.2",
  executionTime = "0.0 s",
  confidence = 95,
  projects = 0,
  backend = "Local",
}) {
  const cards = [
    {
      title: "Active Agents",
      value: activeAgents,
      icon: <Cpu size={18} />,
    },
    {
      title: "Model",
      value: model,
      icon: <Brain size={18} />,
    },
    {
      title: "Execution",
      value: executionTime,
      icon: <Clock3 size={18} />,
    },
    {
      title: "Confidence",
      value: `${confidence}%`,
      icon: <Target size={18} />,
    },
    {
      title: "Projects",
      value: projects,
      icon: <Database size={18} />,
    },
    {
      title: "Backend",
      value: backend,
      icon: <Server size={18} />,
    },
  ];

  return (
    <div className="grid grid-cols-2 gap-3">
      {cards.map((card, index) => (
        <div
          key={index}
          className="rounded-2xl border border-slate-700 bg-[#111827] p-4"
        >
          <div className="flex items-center justify-between">
            <div className="text-slate-400">
              {card.icon}
            </div>
            <span className="text-xs text-slate-500">
              {card.title}
            </span>
          </div>
          <div className="mt-4 text-xl font-bold break-words leading-tight">
            {card.value}
          </div>
        </div>
      ))}
    </div>
  );
}