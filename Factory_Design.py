from abc import ABC, abstractmethod
class Battleship(ABC):
    def __init__(self):
        print("Battleship Created")
    @abstractmethod
    def fire(self):
        pass
    @abstractmethod
    def steer(self):
        pass
    def __del__(self):
        print("Battleship Destroyed")
class Destroyer(Battleship):
    def __init__(self):
        super().__init__()
        print("Destroyer Created")
    def fire(self):
        print("Destroyer Fire")
    def steer(self):
        print("Destroyer Steer")
class Carrier(Battleship):
    def __init__(self):
        super().__init__()
        print("Carrier Created")

    def fire(self):
        print("Carrier Fire")

    def steer(self):
        print("Carrier Steer")
class ShipCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    def create_ship(self):
        return self.factory_method()
class CarrierCreator(ShipCreator):
    def factory_method(self):
        return Carrier()
class DestroyerCreator(ShipCreator):
    def factory_method(self):
        return Destroyer()
if __name__ == "__main__":
    # Create a Carrier using the CarrierCreator
    creator = CarrierCreator()
    battleship1 = creator.create_ship()
    battleship1.fire()
    battleship1.steer()

    print("\nSecond Battleship:\n")
    creator = DestroyerCreator()
    battleship2 = creator.create_ship()
    battleship2.fire()
    battleship2.steer()
