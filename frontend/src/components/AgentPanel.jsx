import { useAgents } from "../context/AgentContext";
import { useTimeline } from "../context/TimelineContext";

import AgentCard from "./AgentCard";
import Timeline from "./Timeline";
import WorkflowGraph from "./WorkflowGraph";
import FileExplorer from "./FileExplorer";
import ResourceDashboard from "./ResourceDashboard";

export default function AgentPanel({
  generatedFiles,
  executionLogs,
  executionTime,
  modelName,
}) {
  const { agents } = useAgents();
  const { events } = useTimeline();

  const files =
    generatedFiles.length
      ? generatedFiles
      : ["frontend/", "backend/", "database/"];

  const logs =
    executionLogs.length
      ? executionLogs.map(
          (log) => `> ${log.command}`
        )
      : [];

  return (
    <div className="w-full h-full overflow-y-auto bg-[#0B1220] border-l border-slate-800">
      <div className="sticky top-0 bg-[#0B1220] border-b border-slate-800 px-6 py-5 z-20">
        <h2 className="text-xl font-bold">
          AI Control Center
        </h2>
        <p className="text-sm text-slate-400">
          Live Company Dashboard
        </p>
      </div>

      <div className="p-4 space-y-3">
        <ResourceDashboard
          activeAgents={Object.keys(agents).length}
          model={modelName}
          executionTime={executionTime}
          projects={files.length}
          backend="Ollama"
        />

        <WorkflowGraph agents={agents} />

        <Timeline events={events} />

        <FileExplorer files={files} />

        {Object.values(agents).map(
          (agent) => (
            <AgentCard
              key={agent.name}
              name={agent.name}
              role={agent.role}
              status={agent.status}
              confidence={agent.confidence || 95}
            />
          )
        )}
      </div>
    </div>
  );
}