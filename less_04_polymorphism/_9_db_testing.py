"""
Создаем класс для тестирования работы с БД

Полиморфизм, который основан на поведении, а не на типе
очень удобен в том числе в тестировании...
Нам не обязательно создавать реальный объект БД или использовать наследование.
Мы можем создавать пустые объекты с нужными атрибутами и методами
...
Хотя понятно, что для серьезного тестирования используются MOCK-и, спец. библиотеки, проверки...
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
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    """ Полиморфная функция
    Считываем из некого Config-file данные о БД и возвращаем экземпляр БД"""
    print("read config")
    return SQLiteDatabase()


class FakeDbForTesting:
    def connect(self):
        pass

    def get_users(self):
        return [1]


if __name__ == '__main__':
    server = Server()
    assert [1] == server.get_users(FakeDbForTesting())  # тестирование

