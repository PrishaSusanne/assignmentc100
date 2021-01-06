class atm(money):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")
        return 1

    def stop(self):
        print("stopped")
        return 2

    def accelerate(self):
        print("accelerating")

    def change_gear(self,gear_type):
        print("gear changed")

# Define some cars
audi = Car("A6", "red", "audi", 80)
print(audi.start())
print(audi.accelerate())
print(audi.stop())
