import {
    Folder,
    FileText,
} from "lucide-react";

export default function FileExplorer({

    files=[],

}){

    return(

        <div className="rounded-2xl border border-slate-700 bg-[#111827] p-5">

            <h3 className="font-semibold mb-5">

                Project Explorer

            </h3>

            <div className="space-y-2">

                {files.map((file,index)=>{

                    const folder=file.endsWith("/");

                    return(

                        <div
                            key={index}
                            className="flex items-center gap-3 text-sm"
                        >

                            {folder
                                ?<Folder
                                    size={17}
                                    className="text-yellow-400"
                                />
                                :<FileText
                                    size={17}
                                    className="text-slate-300"
                                />
                            }

                            <span>

                                {file}

                            </span>

                        </div>

                    )

                })}

            </div>

        </div>

    )

}