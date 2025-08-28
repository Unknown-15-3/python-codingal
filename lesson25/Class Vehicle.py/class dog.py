class dog:
    
    species = "dog"

    def __init__(self, friendly, dangerous):
        self.friendly = friendly
        self.dangerous = dangerous

puppy = dog("puppy", "not dangerous")
bully = dog("bully", "dangerous")

print("puppy is a", puppy.species)
print("bully is also a", bully.species)

print(puppy.friendly, "is", puppy.dangerous)
print(bully.species, "is", bully.dangerous)