import React, { useState, useEffect } from 'react';
import { getBookings } from '../services/api'; // Імпортуємо функцію для отримання всіх бронювань
import './AllBookings.css'; // Стилізуйте сторінку за вашими потребами

const AllBookings = () => {
   const [bookings, setBookings] = useState([]);

   useEffect(() => {
      fetchBookings();
   }, []);

   const fetchBookings = async () => {
      try {
         const response = await getBookings(); // Отримуємо всі бронювання
         setBookings(response.data); // Оновлюємо стан бронювань
      } catch (error) {
         console.error('Error fetching bookings:', error);
      }
   };

   return (
      <div className='all-bookings'>
         <h2>Усі бронювання</h2>
         <table>
            <thead>
               <tr>
                  <th>Водій</th>
                  <th>Клієнт</th>
                  <th>Час бронювання</th>
                  <th>Тривалість</th>
                  <th>Статус</th>
                  <th>Початкова точка</th>
                  <th>Кінцева точка</th>
               </tr>
            </thead>
            <tbody>
               {bookings.map(booking => (
                  <tr key={booking.booking_id}>
                     <td>{booking.booking_driver_ref}</td>
                     <td>{booking.booking_customer_ref}</td>
                     <td>{booking.booking_time}</td>
                     <td>{booking.booking_duration}</td>
                     <td>{booking.booking_status}</td>
                     <td>{booking.booking_start_point}</td>
                     <td>{booking.booking_end_point}</td>
                  </tr>
               ))}
            </tbody>
         </table>
      </div>
   );
};

export default AllBookings;
