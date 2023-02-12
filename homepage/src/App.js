import React from 'react' ; 
import './App.css';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom' ;
import Navbar from './components/Navbar';
import Home from './pages/Products';
import { Products } from './pages/Products';
import { Reports } from './pages/Reports';



function App() {
  return (
    <div>
      <Router>
      <Navbar>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/Products" element = {<Products/>}/>
        <Route path="/Reports" element = {<Reports/>}/> 
      </Routes>
      </Navbar>
      </Router>
    </div>
  );
}

export default App;
