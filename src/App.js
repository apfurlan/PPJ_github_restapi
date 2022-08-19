import React, { useState } from 'react' ;
import Tasks from "./components/Tasks" ;

import './App.css' ; 


const App = () => {
  const [message, setTasks] = useState([
    {
      id: "1",
      title: "Estudar",
      completed: false,
    },
    {
      id: '2',
      title: "Ler Livros" , 
      completed: true, 
    },
  ]);

  return (
    <>
      <div className = "container">
        <Tasks tasks = {tasks} />
      </div>  
    </> 
  ); 
};

// ==== 27:37
export default App ; 