from app.db import Database

class TierInstance:
    def __init__(self, TierID, TierName, TierPrice, TierOrder):
        self.tier_id = TierID
        self.tier_name = TierName
        self.tier_price = TierPrice
        self.tier_order = TierOrder

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
    def get_tier_by_id(tier_id):
        db = Database()
        query = "SELECT * FROM Tiers WHERE TierID = %s"
        result = db.execute_query(query, (tier_id,))
        if result:
            row = result[0]
            return TierInstance(**row)
        return None

    @staticmethod
    def add_tier(tier_name, tier_price, tier_order):
        db = Database()
        query = """
        INSERT INTO Tiers (TierName, TierPrice, TierOrder)
        VALUES (%s, %s, %s)
        """
        db.execute_query(query, (tier_name, tier_price, tier_order))
