from db import Database

class CarInstance:
    def __init__(self, car_id, car_user_ref, car_model, car_tier_ref, car_location):
        self.car_id = car_id
        self.car_user_ref = car_user_ref
        self.car_model = car_model
        self.car_tier_ref = car_tier_ref
        self.car_location = car_location

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
    def add_car(car_user_ref, car_model, car_tier_ref, car_location):
        db = Database()
        query = """
        INSERT INTO Cars (CarUserRef, CarModel, CarTierRef, CarLocation)
        VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (car_user_ref, car_model, car_tier_ref, car_location))
