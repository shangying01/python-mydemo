class Person(object):

    def __init__(self):
        self._age = None
        self._name=None

    def get_age(self):
        return self._age

    def set_age(self, age):
            self._age = int(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
            self._name = name