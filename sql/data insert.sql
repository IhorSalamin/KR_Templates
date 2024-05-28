INSERT INTO Users (UserName, UserEmail, UserPhone, UserPassword, UserGender, UserRole, UserDetails) VALUES
('Іван Іванов', 'ivan@example.com', '0981234567', 'password123', 'Male', 'Customer', 'Some details about Ivan'),
('Петро Петренко', 'petro@example.com', '0677654321', 'password456', 'Male', 'Driver', 'Some details about Petro');

INSERT INTO Cars (CarUserRef, CarModel, CarTierRef, CarLocation) VALUES
(1, 'Toyota Camry', 1, 'Kyiv'),
(1, 'Honda Civic', 2, 'Lviv'),
(2, 'Ford Focus', 3, 'Odessa');

INSERT INTO Tiers (TierName, TierPrice, TierOrder) VALUES
('Economy', 30.00, 1),
('Standard', 50.00, 2),
('Premium', 70.00, 3);

INSERT INTO Bookings (BookingDriverRef, BookingCustomerRef, BookingTime, BookingDuration, BookingStatus, BookingStartPoint, BookingEndPoint) VALUES
(2, 1, '2024-05-10 10:00:00', 5, 'Confirmed', 'Kyiv, Shevchenko St.', 'Lviv, Freedom Ave.'),
(2, 1, '2024-05-12 14:00:00', 6, 'Pending', 'Lviv, Freedom Ave.', 'Kyiv, Shevchenko St.');

INSERT INTO Messages (MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef) VALUES
('2024-05-10 09:30:00', 1, 2, 'High', 'Message content here', 'Attachment link', 1),
('2024-05-12 13:45:00', 2, 1, 'Low', 'Another message content', NULL, 2);

INSERT INTO Rates (RateSenderRef, RateRecipientRef, RateStars, RateDescription) VALUES
(1, 2, 5, 'Excellent service!'),
(2, 1, 4, 'Good customer.');

INSERT INTO Servers (ServerStatus, ServerLocation) VALUES
('Online', 'Kyiv'),
('Offline', 'Lviv');
