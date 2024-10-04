
class First:
    def __init__(self):
        self._login = 'login'
        self.__password = 'password'


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = 'qwerty'
        self.__password = '12345'


"""
Благодаря приватному атрибуту в объекте second СОХРАНЕНЫ ОБА ПАРОЛЯ:

['_First__password',
 '_Second__password',
 ...
 '_login']
 
 Т.Е. двойное подчеркивание и Name mangling
 придуманы для того, чтобы
 при наследовании вы не затёрли значения
 неких важных специализированных атрибутов ПРЕДКА
"""

if __name__ == '__main__':
    first = First()
    second = Second()
    print(second._First__password)  # password
    print(second._Second__password)  # 12345
    # print(dir(second))
