from app.db import Database

class RateInstance:
    def __init__(self, RateID, RateSenderRef, RateRecipientRef, RateStars, RateDescription):
        self.rate_id = RateID
        self.rate_sender_ref = RateSenderRef
        self.rate_recipient_ref = RateRecipientRef
        self.rate_stars = RateStars
        self.rate_description = RateDescription

class Rate:
    @staticmethod
    def get_all_rates():
        db = Database()
        query = "SELECT * FROM Rates"
        results = db.execute_query(query)
        rates = []
        for row in results:
            rates.append(RateInstance(**row))
        return rates

    @staticmethod
    def get_rate_by_id(rate_id):
        db = Database()
        query = "SELECT * FROM Rates WHERE RateID = %s"
        result = db.execute_query(query, (rate_id,))
        if result:
            row = result[0]
            return RateInstance(**row)
        return None

    @staticmethod
    def add_rate(rate_sender_ref, rate_recipient_ref, rate_stars, rate_description):
        db = Database()
        query = """
        INSERT INTO Rates (RateSenderRef, RateRecipientRef, RateStars, RateDescription)
        VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (rate_sender_ref, rate_recipient_ref, rate_stars, rate_description))
