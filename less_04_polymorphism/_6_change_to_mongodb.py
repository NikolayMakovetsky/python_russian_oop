"""
Расширяем функционал сервера для работы с разными БД
"""


class SQLiteDatabase:
    def connect(self):
        print("Connecting to database SQLiteDatabase")

    def get_users(self):
        print("get users with SQL")


class MongoDatabase:
    def connect(self):
        print("Connecting to database MongoDatabase")

    def get_users(self):
        print("get users with NoSQL")


class Server:
    def get_users(self, db):
        """Передаем параметр db для реализации полиморфной функции"""
        db.connect()
        users = db.get_users()
        return users


if __name__ == '__main__':
    server = Server()
    server.get_users(MongoDatabase())
