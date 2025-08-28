#create class
class  vehicle:

    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

    #object creation
modlex = vehicle(240,18)

#access the variations inside the init

print("model max speed:-", modlex.maxspeed)
print("model mileage:-", modlex.mileage)