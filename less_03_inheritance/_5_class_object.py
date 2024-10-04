"""Любой объект в питоне наследуется от базового класса object"""

class Empty:  # под капотом запускается строка class Empty(object):
    pass

if __name__ == '__main__':
    print(dir(Empty()))
