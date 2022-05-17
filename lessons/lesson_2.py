"""
git pull origin main
"""


class Animal:
    voice = 'some'

    def __init__(self, name):
        self.animal_name = name


animal = Animal('Cat')
print(animal.animal_name)


class Animal:
    voice = 'some'
    _voice = 'some'
    __voice = 'voice'

    def get_voice(self):
        print(self.voice)
        print(self._voice)
        print(self.__voice)


class Cat(Animal):
    def say_hello(self):
        print(self.voice)
        print(self._voice)
        print(self._Animal__voice)


animal = Cat()
animal.say_hello()
