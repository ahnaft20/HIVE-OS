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
      return "bg-emerald-500";

    if (status === "Working")
      return "bg-blue-500 animate-pulse";

    if (status === "Planning")
      return "bg-yellow-500";

    return "bg-slate-600";
  }

  return (

    <div className="rounded-2xl border border-slate-700 bg-[#111827] p-4">

      <h3 className="font-semibold mb-6">

        Workflow Graph

      </h3>

      <div className="flex flex-col gap-2">

        {steps.map((step, index) => (

          <div key={step.key}>

            <div className="flex items-center gap-4">

              <div
                className={`w-11 h-11 rounded-full ${color(
                  agents[step.key]?.status
                )} flex items-center justify-center shadow-lg transition-all duration-500`}
              >

                {step.icon}

              </div>

              <div className="flex-1">

                <div className="font-medium">

                  {step.key}

                </div>

              </div>

            </div>

            {index !== steps.length - 1 && (

              <div className="ml-5 h-3 w-px bg-gradient-to-b from-purple-500 to-slate-700"></div>

            )}

          </div>

        ))}

      </div>

    </div>

  );

}