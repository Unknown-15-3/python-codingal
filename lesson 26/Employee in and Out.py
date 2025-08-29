class employee:

    def __init__ (self):
        print("employee created")

    def __del__ (self):
        print("destruction called")

def createobject():
    print("making object")
    obj = employee()
    print("function end")
    return obj

print("calling function creatteobject()...")
obj = createobject()
print("program end...")