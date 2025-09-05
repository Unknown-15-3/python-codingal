class myclass:

    __privatevar = 27

    def __privatemeth(self):
        print("I am inside class myclass")

    def hello(self):
        print("the private variale is:", self.__privatevar)

obj = myclass()
obj.hello()
obj.__privatemeth()