"""
В данном коде плохо то, что наш сервер умеет работать только с конкретной БД
"""

class SQLiteDatabase:
    def connect(self):
        print("Connecting to database SQLiteDatabase")

    def get_users(self):
        print("get users with SQL")


class Server:
    def get_users(self):
        db = SQLiteDatabase()
        db.connect()
        users = db.get_users()
        return users


if __name__ == '__main__':
    server = Server()
    server.get_users()
