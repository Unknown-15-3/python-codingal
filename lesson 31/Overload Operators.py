class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a<other.a):
            return "ob1 is less then ob2"
        else:
            return "ob2 is less then ob1"
        
    def __eq__(self, other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "not equal"
        
ob1 = A(2)
ob2 = A(3)
print("pass values ", ob1.a, ob2.a)
print(ob1<ob2)

ob3 = A(2)
ob4 = A(2)
print("pass values ", ob3.a, ob4.a)
print(ob3==ob4)
    