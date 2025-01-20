
class Car:
    def __init__(self, model, year_of_release, engine_capacity, price, car_mileage, number_of_wheels):
        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.price = price
        self.car_mileage = car_mileage
        self.number_of_wheels = number_of_wheels
        print("Характеристики созданы")

    def descrition(self):
        descrition = (f"Название модели авто - {self.model}, Год выпуска - {self.year_of_release}, "
                  f"Объём двигателя - {self.engine_capacity},"
                  f"Цена - {self.price}, Пробег авто - {self.car_mileage}, "
                  f"Колличество колёс - {self.number_of_wheels}")
        return descrition

crossover = Car("Hyundai","2013",
                "2.0L","15000USD","158000Km","4")

class Truck(Car):
    def __init__(self,model, year_of_release, engine_capacity, price, car_mileage, number_of_wheels):
        super().__init__(model, year_of_release, engine_capacity, price, car_mileage, number_of_wheels)

    def descrition(self):
        descrition = (f"Название модели авто - {self.model}, Год выпуска - {self.year_of_release}, "
                  f"Объём двигателя - {self.engine_capacity},"
                  f"Цена - {self.price}, Пробег авто - {self.car_mileage}, "
                  f"Колличество колёс - {self.number_of_wheels}")
        return descrition

trucks = Truck("Hyundai","2013",
                "2.0L","15000USD","158000Km","8")

print(crossover.descrition())
print(trucks.descrition())








