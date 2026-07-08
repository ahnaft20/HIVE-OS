import {

  createContext,

  useContext,

  useState,

} from "react";

const TimelineContext =

createContext();

export function TimelineProvider({

  children,

}) {

  const [

    events,

    setEvents,

  ] = useState([]);

  function addEvent(

    message,

  ) {

    setEvents(

      (prev) => [

        ...prev,

        {

          time:

            new Date().toLocaleTimeString(),

          message,

        },

      ]

    );

  }

  function clearTimeline() {

    setEvents([]);

  }

  return (

    <TimelineContext.Provider

      value={{

        events,

        addEvent,

        clearTimeline,

      }}

    >

      {children}

    </TimelineContext.Provider>

  );

}

export function useTimeline() {

  return useContext(

    TimelineContext

  );

}