import {
  Brain,
  CheckCircle2,
  Loader2,
  Clock3,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

export default function AgentCard({
  name,
  role,
  status,
  confidence,
}) {

  const statusConfig = {

    Completed: {
      color: "bg-emerald-500",
      badge: "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30",
      icon: <CheckCircle2 size={18} className="text-emerald-400" />,
      width: "100%",
    },

    Working: {
      color: "bg-blue-500",
      badge: "bg-blue-500/20 text-blue-400 border border-blue-500/30",
      icon: <Loader2 size={18} className="animate-spin text-blue-400" />,
      width: "65%",
    },

    Planning: {
      color: "bg-yellow-500",
      badge: "bg-yellow-500/20 text-yellow-400 border border-yellow-500/30",
      icon: <Clock3 size={18} className="text-yellow-400" />,
      width: "35%",
    },

    Waiting: {
      color: "bg-slate-500",
      badge: "bg-slate-500/20 text-slate-300 border border-slate-500/30",
      icon: <Clock3 size={18} className="text-slate-400" />,
      width: "10%",
    },

  };

  const current =
    statusConfig[status] || statusConfig.Waiting;

  return (

    <div className="rounded-3xl border border-slate-700/70 bg-gradient-to-br from-[#111827] to-[#0f172a] p-5 shadow-lg hover:shadow-purple-500/20 hover:border-purple-500 transition-all duration-300 hover:-translate-y-1">

      {/* Header */}

      <div className="flex justify-between items-start">

        <div className="flex gap-3">

          <div className={`w-12 h-12 rounded-2xl ${current.color} flex items-center justify-center shadow-lg`}>

            <Brain size={22} className="text-white" />

          </div>

          <div>

            <h3 className="font-bold text-white">

              {name}

            </h3>

            <p className="text-xs text-slate-400 mt-1">

              {role}

            </p>

          </div>

        </div>

        {current.icon}

      </div>

      {/* Status */}

      <div className="mt-5 flex justify-between items-center">

        <span className="text-xs text-slate-400 uppercase tracking-wider">

          Status

        </span>

        <span className={`px-3 py-1 rounded-full text-xs font-semibold ${current.badge}`}>

          {status}

        </span>

      </div>

      {/* Progress */}

      <div className="mt-3 h-2 rounded-full bg-slate-800 overflow-hidden">

        <div

          className={`${current.color} h-full transition-all duration-700 rounded-full`}

          style={{

            width: current.width,

          }}

        />

      </div>

      {/* Footer */}

      <div className="mt-5 flex justify-between">

        <div className="flex items-center gap-2 text-slate-400 text-sm">

          <ShieldCheck size={16} />

          Confidence

        </div>

        <div className="flex items-center gap-1 font-bold text-purple-400">

          <Sparkles size={15} />

          {confidence}%

        </div>

      </div>

    </div>

  );

}