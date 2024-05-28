from app.db import Database

class CarInstance:
    def __init__(self, CarID, CarUserRef, CarModel, CarTierRef, CarLocation):
        self.car_id = CarID
        self.car_user_ref = CarUserRef
        self.car_model = CarModel
        self.car_tier_ref = CarTierRef
        self.car_location = CarLocation

class Car:
    @staticmethod
    def get_all_cars():
        db = Database()
        query = "SELECT * FROM Cars"
        results = db.execute_query(query)
        cars = []
        for row in results:
            cars.append(CarInstance(**row))
        return cars

    @staticmethod
    def get_car_by_id(car_id):
        db = Database()
        query = "SELECT * FROM Cars WHERE CarID = %s"
        result = db.execute_query(query, (car_id,))
        if result:
            row = result[0]
            return CarInstance(**row)
        return None

    @staticmethod
    def add_car(car_user_ref, car_model, car_tier_ref, car_location):
        db = Database()
        query = """
        INSERT INTO Cars (CarUserRef, CarModel, CarTierRef, CarLocation)
        VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (car_user_ref, car_model, car_tier_ref, car_location))
