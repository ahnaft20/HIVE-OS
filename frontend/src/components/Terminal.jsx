export default function Terminal({

    logs=[],

}){

    return(

        <div className="rounded-2xl border border-slate-700 bg-black p-5">

            <h3 className="text-green-400 font-semibold mb-4">

                Live Terminal

            </h3>

            <div className="font-mono text-sm space-y-2 max-h-56 overflow-y-auto">

                {logs.length===0 &&(

                    <div className="text-slate-500">

                        Waiting for execution...

                    </div>

                )}

                {logs.map(

                    (log,index)=>(

                        <div
                            key={index}
                            className="text-green-400"
                        >

                            {log}

                        </div>

                    )

                )}

            </div>

        </div>

    )

}