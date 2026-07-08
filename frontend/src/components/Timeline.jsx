import { Clock3 } from "lucide-react";

export default function Timeline({

  events = [],

}) {

  return (

    <div className="rounded-2xl bg-[#111827] border border-slate-700 p-5">

      <div className="flex items-center gap-2 mb-5">

        <Clock3
          size={18}
          className="text-purple-400"
        />

        <h3 className="font-semibold">

          Mission Execution

        </h3>

      </div>

      <div className="space-y-4">

        {events.length === 0 && (

          <div className="text-slate-500 text-sm">

            Waiting for mission...

          </div>

        )}

        {events.map(

          (event, index) => (

            <div

              key={index}

              className="flex gap-4"

            >

              <div className="text-xs text-slate-500 w-20">

                {event.time}

              </div>

              <div className="flex-1">

                <div className="rounded-xl border border-slate-700 bg-[#0F172A] px-4 py-3 hover:border-purple-500 transition-all duration-300">

                  <div className="flex items-center gap-2">

                    <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>

                    <span className="text-sm">

                      {event.message}

                    </span>

                  </div>

                </div>

              </div>

            </div>

          )

        )}

      </div>

    </div>

  );

}