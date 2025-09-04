class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

schoolbus = bus("school volvo", 180, 12)
print("vehicle name:-", schoolbus.name)
print("max soeed:-", schoolbus.maxspeed)
print("mileage:-", schoolbus.mileage)