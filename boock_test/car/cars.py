
class Car:

    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает название марку и модель автомобиля."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег автомобиля."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Обновляет пробег автомобля."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Инкрементирует пробег."""
        self.odometer_reading += miles


class ElectricCar(Car):

    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class Battery:

    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


my_car = Car(make='BMW', model='7', year=1990)
tesla = ElectricCar(make='Ford', model='Kuga', year=2019)

new_tesla = ElectricCar(make='Ford2', model='Kuga2', year=2019)
new_tesla.battery.get_range()
new_tesla.battery.update_battery()
new_tesla.battery.get_range()
