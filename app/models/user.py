from db import Database

class UserInstance:
    def __init__(self, user_id, user_name, user_email, user_phone, user_password, user_gender, user_role, user_details):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_password = user_password
        self.user_gender = user_gender
        self.user_role = user_role
        self.user_details = user_details

class User:
    @staticmethod
    def get_user_by_id(user_id):
        db = Database()
        query = "SELECT * FROM Users WHERE UserID = %s"
        result = db.execute_query(query, (user_id,))
        if result:
            row = result[0]
            return UserInstance(**row)
        return None

    @staticmethod
    def create_user(user_name, user_email, user_phone, user_password, user_gender, user_role, user_details):
        db = Database()
        query = """
        INSERT INTO Users (UserName, UserEmail, UserPhone, UserPassword, UserGender, UserRole, UserDetails)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        db.execute_query(query, (user_name, user_email, user_phone, user_password, user_gender, user_role, user_details))

    @staticmethod
    def get_all_users():
        db = Database()
        query = "SELECT * FROM Users"
        results = db.execute_query(query)
        users = []
        for row in results:
            users.append(UserInstance(**row))
        return users
