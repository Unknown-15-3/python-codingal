class vehicle:

    def __init__(vehicleType):
        print("vehicle type is:", vehicleType)

class car(vehicle):

    def __init__(self):
        super().__init__(car)

print(issubclass(car, vehicle))
print(issubclass(car, list))
print(issubclass(car, car))
print(issubclass(car, (list, vehicle)))