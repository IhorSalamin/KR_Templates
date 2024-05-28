from app.db import Database

class BookingInstance:
    def __init__(self, BookingID, BookingDriverRef, BookingCustomerRef, BookingTime, BookingDuration, BookingStatus, BookingStartPoint, BookingEndPoint):
        self.booking_id = BookingID
        self.booking_driver_ref = BookingDriverRef
        self.booking_customer_ref = BookingCustomerRef
        self.booking_time = BookingTime
        self.booking_duration = BookingDuration
        self.booking_status = BookingStatus
        self.booking_start_point = BookingStartPoint
        self.booking_end_point = BookingEndPoint

class Booking:
    @staticmethod
    def get_all_bookings():
        db = Database()
        query = "SELECT * FROM Bookings"
        results = db.execute_query(query)
        bookings = []
        for row in results:
            bookings.append(BookingInstance(**row))
        return bookings

    @staticmethod
    def get_booking_by_id(booking_id):
        db = Database()
        query = "SELECT * FROM Bookings WHERE BookingID = %s"
        result = db.execute_query(query, (booking_id,))
        if result:
            row = result[0]
            return BookingInstance(**row)
        return None

    @staticmethod
    def create_booking(booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point):
        db = Database()
        query = """
        INSERT INTO Bookings (BookingDriverRef, BookingCustomerRef, BookingTime, BookingDuration, BookingStatus, BookingStartPoint, BookingEndPoint)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        db.execute_query(query, (booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point))
