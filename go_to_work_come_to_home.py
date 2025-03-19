class Alarm:
    def alarm_on(self):
        print("Alarm is on and the house is secured.")

    def alarm_off(self):
        print("Alarm is off, and you can go into the house.")


class AirConditioner:
    def air_on(self):
        print("Air conditioner is on.")

    def air_off(self):
        print("Air conditioner is off.")


class TV:
    def tv_on(self):
        print("TV is on.")

    def tv_off(self):
        print("TV is off.")


class HouseFacade:
    def __init__(self):  # Fixed constructor name
        self.alarm = Alarm()
        self.ac = AirConditioner()
        self.tv = TV()

    def go_to_work(self):
        print("Going to work:")
        self.ac.air_off()  # Fixed method name
        self.tv.tv_off()
        self.alarm.alarm_on()

    def come_home(self):
        print("\nGot home:")
        self.ac.air_on()  # Fixed method name
        self.tv.tv_on()
        self.alarm.alarm_off()


# Fixed main execution check
if __name__ == "__main__":
    house = HouseFacade()
    house.go_to_work()
    house.come_home()
