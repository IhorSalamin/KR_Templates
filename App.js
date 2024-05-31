import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CarList from './components/CarList';
import RegisterClient from './pages/RegisterClient';
import CreateBooking from './pages/CreateBooking';
import Navigation from './components/Navigation';
import './App.css';

const App = () => {
   return (
      <Router>
         <div className="app">
            <h1 className="head">Система прокату автомобілів</h1>
            <Navigation />
            <Routes>
               <Route path="/cars" element={<CarList />} />
               <Route path="/register-client" element={<RegisterClient />} />
               <Route path="/create-booking" element={<CreateBooking />} />
            </Routes>
         </div>
      </Router>
   );
};

export default App;
