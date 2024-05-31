import React, { useState, useEffect } from 'react';
import { createBooking, getClients } from '../services/api';
import './CreateBooking.css';

const CreateBooking = () => {
   const [bookingData, setBookingData] = useState({
      booking_driver_ref: '',
      booking_customer_ref: '',
      booking_time: '',
      booking_duration: '',
      booking_status: '',
      booking_start_point: '',
      booking_end_point: ''
   });

   const [clients, setClients] = useState([]);

   useEffect(() => {
      fetchClients();
   }, []);

   const fetchClients = async () => {
      try {
         const response = await getClients();
         setClients(response.data);
      } catch (error) {
         console.error('Error fetching clients:', error);
      }
   };

   const handleChange = (e) => {
      const { name, value } = e.target;
      setBookingData(prevState => ({ ...prevState, [name]: value }));
   };

   const handleSubmit = (e) => {
      e.preventDefault();
      createBooking(bookingData).then(() => {
         alert('Бронювання створено успішно');
         setBookingData({
            booking_driver_ref: '',
            booking_customer_ref: '',
            booking_time: '',
            booking_duration: '',
            booking_status: '',
            booking_start_point: '',
            booking_end_point: ''
         });
      }).catch(error => {
         console.error('Error creating booking:', error);
      });
   };

   return (
      <div className='one'>
         <h2>Створення бронювання</h2>
         <form onSubmit={handleSubmit}>
            <fieldset>
               <select
                  name="booking_driver_ref"
                  value={bookingData.booking_driver_ref}
                  onChange={handleChange}
                  required
               >
                  <option value="">Виберіть водія</option>
                  {clients.map(client => (
                     <option key={client.id} value={client.id}>
                        {client.id}
                     </option>
                  ))}
               </select>
               <input
                  type="text"
                  name="booking_customer_ref"
                  value={bookingData.booking_customer_ref}
                  onChange={handleChange}
                  placeholder="Booking Customer Ref"
                  required
               />
               <input
                  type="datetime-local"
                  name="booking_time"
                  value={bookingData.booking_time}
                  onChange={handleChange}
                  placeholder="Booking Time"
                  required
               />
               <input
                  type="text"
                  name="booking_duration"
                  value={bookingData.booking_duration}
                  onChange={handleChange}
                  placeholder="Booking Duration"
                  required
               />
               <input
                  type="text"
                  name="booking_status"
                  value={bookingData.booking_status}
                  onChange={handleChange}
                  placeholder="Booking Status"
                  required
               />
               <input
                  type="text"
                  name="booking_start_point"
                  value={bookingData.booking_start_point}
                  onChange={handleChange}
                  placeholder="Booking Start Point"
                  required
               />
               <input
                  type="text"
                  name="booking_end_point"
                  value={bookingData.booking_end_point}
                  onChange={handleChange}
                  placeholder="Booking End Point"
               />
               <button type="submit">Створити бронювання</button>
            </fieldset>
         </form>
      </div>
   );
};

export default CreateBooking;

