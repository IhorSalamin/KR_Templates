from app.db import Database

class ServerInstance:
    def __init__(self, ServerID, ServerStatus, ServerLocation):
        self.server_id = ServerID
        self.server_status = ServerStatus
        self.server_location = ServerLocation

class Server:
    @staticmethod
    def get_all_servers():
        db = Database()
        query = "SELECT * FROM Servers"
        results = db.execute_query(query)
        servers = []
        for row in results:
            servers.append(ServerInstance(**row))
        return servers

    @staticmethod
    def get_server_by_id(server_id):
        db = Database()
        query = "SELECT * FROM Servers WHERE ServerID = %s"
        result = db.execute_query(query, (server_id,))
        if result:
            row = result[0]
            return ServerInstance(**row)
        return None

    @staticmethod
    def add_server(server_status, server_location):
        db = Database()
        query = """
        INSERT INTO Servers (ServerStatus, ServerLocation)
        VALUES (%s, %s)
        """
        db.execute_query(query, (server_status, server_location))
