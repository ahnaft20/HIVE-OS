import { CheckCircle2 } from "lucide-react";

export default function WorkflowGraph({ agents }) {

  const steps = [
    { key: "Research", icon: "🧠" },
    { key: "Engineer", icon: "💻" },
    { key: "Designer", icon: "🎨" },
    { key: "Documentation", icon: "📄" },
    { key: "QA", icon: "🧪" },
    { key: "Leader", icon: "👑" },
  ];

  function color(status) {

    if (status === "Completed")
      return "bg-emerald-500 shadow-emerald-500/50 shadow-lg";

    if (status === "Working" || status === "Reviewing")
      return "bg-blue-500 animate-pulse shadow-blue-500/50 shadow-lg";

    if (status === "Planning")
      return "bg-yellow-500 animate-pulse";

    return "bg-slate-600";

  }

  return (

    <div className="rounded-2xl border border-slate-700 bg-[#111827] p-4">

      <h3 className="font-semibold mb-6">

        Workflow Graph

      </h3>

      <div className="flex flex-col gap-2">

        {steps.map((step, index) => {

          const status = agents[step.key]?.status;

          return (

            <div key={step.key}>

              <div className="flex items-center gap-4">

                <div
                  className={`w-11 h-11 rounded-full ${color(status)} flex items-center justify-center transition-all duration-500`}
                >

                  {status === "Completed"
                    ? <CheckCircle2 size={20} />
                    : step.icon}

                </div>

                <div className="flex-1">

                  <div className="font-medium">

                    {step.key}

                  </div>

                  <div className="text-xs text-slate-400">

                    {status || "Waiting"}

                  </div>

                </div>

              </div>

              {index !== steps.length - 1 && (

                <div
                  className={`ml-5 h-6 w-px transition-all duration-500 ${
                    status === "Completed"
                      ? "bg-emerald-500"
                      : "bg-gradient-to-b from-purple-500 to-slate-700"
                  }`}
                />

              )}

            </div>

          );

        })}

      </div>

    </div>

  );

}