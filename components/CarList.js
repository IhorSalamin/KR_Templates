import React, { useState, useEffect } from 'react';
import { getCars } from '../services/api'; // Імпортуємо функцію для отримання всіх автомобілів
import './CarList.css'

const AllCars = () => {
   const [cars, setCars] = useState([]);

   useEffect(() => {
      fetchCars();
   }, []);

   const fetchCars = async () => {
      try {
         const response = await getCars(); // Отримуємо всі автомобілі
         setCars(response.data); // Оновлюємо стан автомобілів
      } catch (error) {
         console.error('Error fetching cars:', error);
      }
   };

   return (
      <div className='all-cars'>
         <h2>Всі автомобілі</h2>
         <table>
            <thead>
               <tr>
                  <th>користувач</th>
                  <th>Модель</th>
                  <th>Категорія</th>
                  <th>Місцезнаходження</th>
               </tr>
            </thead>
            <tbody>
               {cars.map(car => (
                  <tr key={car.car_id}>
                     <td>{car.car_user_ref}</td>
                     <td>{car.car_model}</td>
                     <td>{car.car_tier_ref}</td>
                     <td>{car.car_location}</td>
                  </tr>
               ))}
            </tbody>
         </table>
      </div>
   );
};

export default AllCars;
