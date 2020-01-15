class Car:

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор


class Garage:
    def __init__(self, cars):
        self.cars = cars

    def add(self, car):
        self.cars.append(car)

    def delete(self, car_idx):
        self.cars.pop(car_idx)

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
