import {
  Cpu,
  ShieldCheck,
} from "lucide-react";

export default function Header() {

  return (

    <header className="h-20 border-b border-slate-800 bg-[#0B1220]/80 backdrop-blur-xl flex items-center justify-between px-8">

      <div>

        <div className="flex items-center gap-3">

          <Cpu
            size={28}
            className="text-purple-400"
          />

          <h1 className="text-3xl font-bold tracking-wide">

            HIVE OS

          </h1>

        </div>

      </div>

      <div className="flex items-center gap-3">

        <div className="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-4 py-2 flex items-center gap-2">

          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />

          <span className="text-emerald-300 text-sm font-medium">

            System Ready

          </span>

        </div>

        <div className="rounded-xl bg-[#111827] border border-slate-700 px-4 py-2 flex items-center gap-2">

          <ShieldCheck size={16} />

          <span className="text-sm">

            DeepSeek V4 Flash

          </span>

        </div>

      </div>

    </header>

  );

}