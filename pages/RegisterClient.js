import React, { useState } from 'react';
import { createClient } from '../services/api';
import './RegisterClient.css'
const RegisterClient = () => {
   const [clientData, setClientData] = useState({
      name: '',
      address: '',
      phone: ''
   });

   const handleChange = (e) => {
      const { name, value } = e.target;
      setClientData(prevState => ({ ...prevState, [name]: value }));
   };

   const handleSubmit = (e) => {
      e.preventDefault();
      createClient(clientData).then(() => {
         alert('Клієнт зареєстрований успішно');
         setClientData({ name: '', address: '', phone: '' });
      }).catch(error => {
         console.error('Error creating client:', error);
      });
   };

   return (
      <div  className='two'>
         <h2>Реєстрація клієнта</h2>
         <form onSubmit={handleSubmit}>
         <fieldset>
            
            <input
               type="text"
               name="name"
               value={clientData.name}
               onChange={handleChange}
               placeholder="Ім'я"
               required
            />
            <input
               type="text"
               name="address"
               value={clientData.address}
               onChange={handleChange}
               placeholder="Адреса"
               required
            />
            <input
               type="text"
               name="phone"
               value={clientData.phone}
               onChange={handleChange}
               placeholder="Телефон"
               required
            />
            <button type="submit">Зареєструвати</button>
            </fieldset>
         </form>
      </div>
   );
};

export default RegisterClient;
