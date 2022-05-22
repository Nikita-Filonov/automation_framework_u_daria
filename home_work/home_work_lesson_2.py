"""
На месте элипсоидов ``...`` нужно написать свою реализацию.
Методы классов должны выводить значения, как указано ниже
"""


class Car:
    doors = 2
    wheels = 4

    def number_of_wheels(self):
        return self.wheels  # тут твоя реализация

    def number_of_doors(self):
        return self.doors  # тут твоя реализация


class BMW(Car):
    doors = 3

    def check_oil(self, oil: str):
        return f'The oil is about {oil}'


class Audi(Car):
    doors = 4
    wheels = 5

    def check_speed(self, speed: str):
        return f'This speed is about {speed}'


bmw_x3 = BMW()
audi_a6 = Audi()

print(bmw_x3.number_of_wheels())  # должно распечатать 4
print(audi_a6.number_of_wheels())  # должно распечатать 5

print(bmw_x3.number_of_doors())  # должно распечатать 3
print(audi_a6.number_of_doors())  # должно распечатать 4

print(bmw_x3.check_oil("1/3"))  # должно распечатать "The oil is about 1/3"
print(audi_a6.check_speed("220 km/h"))  # должно распечатать "This speed is about 220 km/h"
