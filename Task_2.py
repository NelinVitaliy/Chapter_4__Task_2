
class Airplane:
    def __init__(self, make, model, year, max_speed, odometr, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = odometr
        self.is_flying = is_flying

    def take_off(self):
        if self.is_flying == False:
            print(f"Самолет сейчас на земле!!")
        else:
            print(f"Самолет {self.model} начинает взлет. Престените ремни безопасности!!!")

    def fly(self):
        print(f"Наш {self.model} набрал максимальную скорость {self.max_speed} киллометров.")
        print(f"Пройденный путь составил {self.odometr} киллометров.")

    def land(self):
        if self.is_flying == False:
            print(f"Самолет сейчас на земле!!")
        else:
            print(f"Самолет {self.model} удачно приземлился. Спасибо что выбрали нашу авиакомпанию.")

    def info_airplane(self):
        print(f"Самолет {self.model} {self.year}. Произведенный в {self.make}, максимальной скорости {self.max_speed} киллометров в час.\n")



boeing = Airplane('USA','Boeing-737', 2010, 850, 3000, True)
boeing.take_off()
boeing.fly()
boeing.land()
boeing.info_airplane()

airbus = Airplane('CAN', 'Airbus A-320', 2013, 800, 1000, False)
airbus.take_off()
airbus.fly()
airbus.land()
airbus.info_airplane()