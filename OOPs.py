class Oops:
    def __init__(self, name, age):
        print("This is the constructor method")
        self.name = name
        self.age = age

    def demomethod(self):
        print("My name is", self.name)
        print("My age is", self.age)


class childOops(Oops):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


obj1 = childOops('Aadriti', 21, 'Black')
obj1.demoMethod()