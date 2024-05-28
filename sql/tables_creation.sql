CREATE DATABASE CarRental;
USE CarRental;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    UserEmail VARCHAR(255) NOT NULL,
    UserPhone VARCHAR(20) NOT NULL,
    UserPassword VARCHAR(255) NOT NULL,
    UserGender VARCHAR(10),
    UserRole VARCHAR(50),
    UserDetails TEXT
);

CREATE TABLE Cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY,
    CarUserRef INT,
    CarModel VARCHAR(100) NOT NULL,
    CarTierRef INT,
    CarLocation VARCHAR(255),
    FOREIGN KEY (CarUserRef) REFERENCES Users(UserID)
);

CREATE TABLE Tiers (
    TierID INT AUTO_INCREMENT PRIMARY KEY,
    TierName VARCHAR(100) NOT NULL,
    TierPrice DECIMAL(10, 2) NOT NULL,
    TierOrder INT NOT NULL
);

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    BookingDriverRef INT,
    BookingCustomerRef INT,
    BookingTime DATETIME NOT NULL,
    BookingDuration INT NOT NULL,
    BookingStatus VARCHAR(50) NOT NULL,
    BookingStartPoint VARCHAR(255) NOT NULL,
    BookingEndPoint VARCHAR(255),
    FOREIGN KEY (BookingDriverRef) REFERENCES Users(UserID),
    FOREIGN KEY (BookingCustomerRef) REFERENCES Users(UserID)
);

CREATE TABLE Messages (
    MessageID INT AUTO_INCREMENT PRIMARY KEY,
    MessageTime DATETIME NOT NULL,
    MessageSenderRef INT,
    MessageRecipientRef INT,
    MessagePriority VARCHAR(50),
    MessageContext TEXT,
    MessageAttachments TEXT,
    MessageBookingRef INT,
    FOREIGN KEY (MessageSenderRef) REFERENCES Users(UserID),
    FOREIGN KEY (MessageRecipientRef) REFERENCES Users(UserID),
    FOREIGN KEY (MessageBookingRef) REFERENCES Bookings(BookingID)
);

CREATE TABLE Rates (
    RateID INT AUTO_INCREMENT PRIMARY KEY,
    RateSenderRef INT,
    RateRecipientRef INT,
    RateStars INT NOT NULL,
    RateDescription TEXT,
    FOREIGN KEY (RateSenderRef) REFERENCES Users(UserID),
    FOREIGN KEY (RateRecipientRef) REFERENCES Users(UserID)
);

CREATE TABLE Servers (
    ServerID INT AUTO_INCREMENT PRIMARY KEY,
    ServerStatus VARCHAR(50),
    ServerLocation VARCHAR(255)
);
