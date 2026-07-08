import { useEffect, useState } from "react";

export default function Terminal({ logs = [] }) {

  const [displayLogs, setDisplayLogs] = useState([]);

  useEffect(() => {

    if (logs.length > 0) {
      setDisplayLogs(logs);
      return;
    }

    const demoLogs = [
      "[Research] Starting mission...",
      "✔ Research Complete",
      "[Engineer] Designing system...",
      "✔ Architecture Generated",
      "[Designer] Creating UI...",
      "✔ UI Completed",
      "[Documentation] Writing documentation...",
      "✔ Documentation Ready",
      "[QA] Running review...",
      "✔ QA Passed",
      "[CEO] Final approval...",
      "✔ Mission Approved",
    ];

    setDisplayLogs([]);

    let index = 0;

    const timer = setInterval(() => {

      setDisplayLogs((prev) => [
        ...prev,
        demoLogs[index],
      ]);

      index++;

      if (index >= demoLogs.length) {
        clearInterval(timer);
      }

    }, 450);

    return () => clearInterval(timer);

  }, [logs]);

  return (

    <div className="rounded-2xl border border-slate-700 bg-black p-5">

      <h3 className="text-green-400 font-semibold mb-4">

        Live Terminal

      </h3>

      <div className="font-mono text-sm space-y-2 max-h-56 overflow-y-auto">

        {displayLogs.map((log, index) => (

          <div
            key={index}
            className="text-green-400"
          >
            {log}
          </div>

        ))}

      </div>

    </div>

  );

}