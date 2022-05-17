class Car:
    doors = 2
    wheels = 4

    def number_of_wheels(self):
        ...  # тут твоя реализация

    def number_of_doors(self):
        ...  # тут твоя реализация


class BMW(Car):
    def check_oil(self, oil: str):
        pass


class Audi(Car):
    def check_speed(self, speed: str):
        pass


bmw_x3 = BMW()
audi_a6 = Audi()

print(bmw_x3.number_of_wheels())  # должно распечатать 4
print(audi_a6.number_of_wheels())  # должно распечатать 5

print(bmw_x3.number_of_doors())  # должно распечатать 3
print(audi_a6.number_of_doors())  # должно распечатать 4

print(bmw_x3.check_oil("1/3"))  # должно распечатать "The oil is about 1/3"
print(audi_a6.check_speed("220 km/h"))  # должно распечатать "This speed is about 220 km/h"
