class car:
    def __init__(a,name):
        a.name=name
    def getData(a):
        a.name=input("Enter the Car company Name: ")
        a.modelname=input("Enter the model name: ")
class model(car):
    def __init__(a,modelname):
        a.modelname=modelname
    def display(a):
        print("Car Company :", a.name)
        print("Car Model :", a.modelname)

obj=model("")
obj.getData()
obj.display()