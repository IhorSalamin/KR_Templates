from db import Database

class BookingInstance:
    def __init__(self, booking_id, booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point):
        self.booking_id = booking_id
        self.booking_driver_ref = booking_driver_ref
        self.booking_customer_ref = booking_customer_ref
        self.booking_time = booking_time
        self.booking_duration = booking_duration
        self.booking_status = booking_status
        self.booking_start_point = booking_start_point
        self.booking_end_point = booking_end_point

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
    def create_booking(booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point):
        db = Database()
        query = """
        INSERT INTO Bookings (BookingDriverRef, BookingCustomerRef, BookingTime, BookingDuration, BookingStatus, BookingStartPoint, BookingEndPoint)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        db.execute_query(query, (booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point))
