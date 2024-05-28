from db import Database

class TierInstance:
    def __init__(self, tier_id, tier_name, tier_price, tier_order):
        self.tier_id = tier_id
        self.tier_name = tier_name
        self.tier_price = tier_price
        self.tier_order = tier_order

class Tier:
    @staticmethod
    def get_all_tiers():
        db = Database()
        query = "SELECT * FROM Tiers"
        results = db.execute_query(query)
        tiers = []
        for row in results:
            tiers.append(TierInstance(**row))
        return tiers

    @staticmethod
    def add_tier(tier_name, tier_price, tier_order):
        db = Database()
        query = """
        INSERT INTO Tiers (TierName, TierPrice, TierOrder)
        VALUES (%s, %s, %s)
        """
        db.execute_query(query, (tier_name, tier_price, tier_order))
