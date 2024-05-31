import React, { useEffect, useState } from 'react';
import { getCars } from '../services/api';

const CarList = () => {
   const [cars, setCars] = useState([]);

   useEffect(() => {
      getCars().then(response => setCars(response.data));
   }, []);

   return (
      <div>
         <h2>Список автомобілів</h2>
         <ul>
            {cars.map(car => (
               <li key={car.id}>{car.car_model} - {car.car_tier_ref}</li>
            ))}
         </ul>
      </div>
   );
};

export default CarList;
