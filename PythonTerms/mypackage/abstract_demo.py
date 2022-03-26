from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
