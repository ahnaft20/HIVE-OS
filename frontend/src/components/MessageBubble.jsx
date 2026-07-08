export default function MessageBubble({

role,

text,

}){

const user=role==="user";

return(

<div

className={`

flex

${user?"justify-end":"justify-start"}

my-6

opacity-0

animate-[fadeInUp_.45s_ease_forwards]

`}

>

<div

className={`

max-w-4xl

rounded-3xl

px-6

py-5

leading-8

shadow-xl

transition-all

duration-300

hover:shadow-purple-500/20

${

user

?

"bg-gradient-to-r from-purple-600 to-violet-600 text-white"

:

"bg-[#111827] border border-slate-700 text-slate-100"

}

`}

>

{text}

</div>

</div>

)

}