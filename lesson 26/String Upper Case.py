class IOString():
    
    def __init__ (self):
        self.strt = ""

    def getstring(self):
        self.strt = input("Enter a string:")

    def printstring(self):
        print("the result i:", self.strt.upper())

strt = IOString()

strt.getstring()
strt.printstring()