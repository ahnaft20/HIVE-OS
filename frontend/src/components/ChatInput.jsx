import { useState } from "react";

import {

SendHorizontal,

Sparkles,

} from "lucide-react";

export default function ChatInput({

onSend,

loading,

}){

const[

text,

setText,

]=useState("");

function submit(){

if(!text.trim()) return;

onSend(text);

setText("");

}

return(

<div className="border-t border-slate-800 bg-[#0B1220]/80 backdrop-blur-xl px-8 py-2">

<div className="max-w-5xl mx-auto">

<div className="rounded-3xl border border-slate-700 bg-gradient-to-br from-[#111827] to-[#0F172A] shadow-xl hover:border-purple-500 transition-all duration-300 flex items-center gap-3 px-5 py-2.5">

<textarea

spellCheck={false}

rows={1}

value={text}

placeholder="Describe the software you want to build..."

onChange={

e=>setText(

e.target.value

)

}

onKeyDown={e=>{

if(

e.key==="Enter"

&&

!e.shiftKey

){

e.preventDefault();

submit();

}

}}

className="flex-1 bg-transparent resize-none outline-none text-white placeholder:text-slate-500 px-2 py-0.5 text-[15px] leading-5"

/>

<button

onClick={submit}

disabled={loading}

className={`rounded-2xl px-5 py-2.5 flex items-center gap-2 transition ${

loading

?

"bg-slate-700"

:

"bg-purple-600 hover:bg-purple-700"

}`}

>

{

loading

?

<>

<Sparkles

size={18}

className="animate-spin"

/>

Thinking

</>

:

<>

<SendHorizontal size={18}/>

Execute

</>

}

</button>

</div>

</div>

</div>

)

}