# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Cars:
    def __init__(self, name, color, speed, is_police=False):
        self.carname = name
        self.paint = color
        self.pace = speed
        self.police = is_police
        print("Initialized")

    def go(self):
        print("Car go")

    def stop(self):
        print("Car stop")

    def turn(self, direction):
        print("Turn to ", direction)


class TownCar(Cars):
    def __init__(self, name, color, speed, is_honk):
        super().__init__(name, color, speed)
        self.having_honk = is_honk

    def honk(self, honk_volume):
        print("Honking at the level of: ", honk_volume)


class SportCar(Cars):
    def __init__(self, name, color, speed, is_nitro):
        super(SportCar, self).__init__(name, color, speed)
        self.nitro = is_nitro

    def nitro(self, level):
        print("Nitro level set to: ", level)


class WorkCar(Cars):
    def tow(self, upside):
        print("Tow is lifted: ", upside)


class PoliceCar(Cars):
    def signal(self, volume):
        print("WEEEHOOWEEEHOOO, volume set to:", volume)


towncar = TownCar("Just Car", "blue", 15, False)
sportcar = SportCar("speedy", "white", 150, False)
workcar = WorkCar("Towing", "rusty", 10, False)
policecar = PoliceCar("Cops", "blue", 100, True)

policecar.go()
policecar.signal(10)



