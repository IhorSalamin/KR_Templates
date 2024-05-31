import React, { useState } from 'react';
import { createClient } from '../services/api';
import './RegisterClient.css'

const RegisterClient = () => {
   const [clientData, setClientData] = useState({
      user_name: '',
      user_email: '',
      user_phone: '',
      user_password: '',
      user_gender: '',
      user_role: '',
      user_details: ''
   });

   const handleChange = (e) => {
      const { name, value } = e.target;
      setClientData(prevState => ({ ...prevState, [name]: value }));
   };

   const handleSubmit = (e) => {
      e.preventDefault();
      createClient(clientData).then(() => {
         alert('Клієнт зареєстрований успішно');
         setClientData({
            user_name: '',
            user_email: '',
            user_phone: '',
            user_password: '',
            user_gender: '',
            user_role: '',
            user_details: ''
         });
      }).catch(error => {
         console.error('Error creating client:', error);
      });
   };

   return (
      <div className='two'>
         <h2>Реєстрація клієнта</h2>
         <form onSubmit={handleSubmit}>
            <fieldset>
               <input
                  type="text"
                  name="user_name"
                  value={clientData.user_name}
                  onChange={handleChange}
                  placeholder="Ім'я"
                  required
               />
               <input
                  type="email"
                  name="user_email"
                  value={clientData.user_email}
                  onChange={handleChange}
                  placeholder="Електронна пошта"
                  required
               />
               <input
                  type="text"
                  name="user_phone"
                  value={clientData.user_phone}
                  onChange={handleChange}
                  placeholder="Телефон"
                  required
               />
               <input
                  type="password"
                  name="user_password"
                  value={clientData.user_password}
                  onChange={handleChange}
                  placeholder="Пароль"
                  required
               />
               <input
                  type="text"
                  name="user_gender"
                  value={clientData.user_gender}
                  onChange={handleChange}
                  placeholder="Стать"
               />
               <input
                  type="text"
                  name="user_role"
                  value={clientData.user_role}
                  onChange={handleChange}
                  placeholder="Роль"
               />
               <input
                  type="text"
                  name="user_details"
                  value={clientData.user_details}
                  onChange={handleChange}
                  placeholder="Деталі"
               />
               <button type="submit">Зареєструвати</button>
            </fieldset>
         </form>
      </div>
   );
};

export default RegisterClient;
