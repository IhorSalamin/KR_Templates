from db import Database

class ServerInstance:
    def __init__(self, server_id, server_status, server_location):
        self.server_id = server_id
        self.server_status = server_status
        self.server_location = server_location

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
    def add_server(server_status, server_location):
        db = Database()
        query = """
        INSERT INTO Servers (ServerStatus, ServerLocation)
        VALUES (%s, %s)
        """
        db.execute_query(query, (server_status, server_location))
