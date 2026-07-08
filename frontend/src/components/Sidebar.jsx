import {

LayoutDashboard,

FolderKanban,

History,

Settings,

} from "lucide-react";

export default function Sidebar(){

const menu = [

  {

    icon:<LayoutDashboard size={20}/>,

    title:"Workspace",

  },

  {

    icon:<FolderKanban size={20}/>,

    title:"Projects",

  },

  {

    icon:<History size={20}/>,

    title:"Execution",

  },

  {

    icon:<Settings size={20}/>,

    title:"Settings",

  },

];

return(

<div className="h-full bg-[#0B1220] border-r border-slate-800 flex flex-col">

<div className="px-6 py-8">

<h2 className="text-4xl font-extrabold tracking-wide">

HIVE

</h2>

<p className="text-slate-400 mt-2 leading-6">

Autonomous

AI Software Company

</p>

</div>

<div className="flex-1 px-4 space-y-2">

{

menu.map(

(item,index)=>(

<button

key={index}

className="w-full rounded-2xl px-4 py-3 flex items-center gap-3 hover:bg-purple-600/20 hover:border-purple-500 border border-transparent transition-all duration-300 hover:translate-x-1"

>

{item.icon}

{item.title}

</button>

)

)

}

</div>

<div className="p-5 text-xs text-slate-500">

HIVE OS v1.0

</div>

</div>

)

}