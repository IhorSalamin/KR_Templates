from db import Database

class RateInstance:
    def __init__(self, rate_id, rate_sender_ref, rate_recipient_ref, rate_stars, rate_description):
        self.rate_id = rate_id
        self.rate_sender_ref = rate_sender_ref
        self.rate_recipient_ref = rate_recipient_ref
        self.rate_stars = rate_stars
        self.rate_description = rate_description

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
    def add_rate(rate_sender_ref, rate_recipient_ref, rate_stars, rate_description):
        db = Database()
        query = """
        INSERT INTO Rates (RateSenderRef, RateRecipientRef, RateStars, RateDescription)
        VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (rate_sender_ref, rate_recipient_ref, rate_stars, rate_description))
