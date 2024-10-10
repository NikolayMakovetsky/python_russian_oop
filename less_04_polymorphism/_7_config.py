"""
Добавляем полиморфную функцию get_db_from_config()
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
        """Передаем параметр db для реализации полиморфной функции
        ТРЕБОВАНИЯ К ОБЪЕКТУ db:
        РЕАЛИЗОВАННЫЕ МЕТОДЫ .connect() .get_users()"""
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    """ Полиморфная функция
    Считываем из некого Config-file данные о БД и возвращаем экземпляр БД"""
    print("read config")
    return SQLiteDatabase()


if __name__ == '__main__':
    server = Server()
    server.get_users(get_db_from_config())  # Передаем результат серверу
