import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navigation.css';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/cars">Список автомобілів</NavLink>
        </li>
        <li>
          <NavLink to="/register-client">Реєстрація клієнта</NavLink>
        </li>
        <li>
          <NavLink to="/create-booking">Створити бронювання</NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
