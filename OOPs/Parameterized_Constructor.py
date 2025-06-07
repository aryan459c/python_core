class Parameterized_Constructor:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def test(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Mobile :", self.number)


c = Parameterized_Constructor(name="Sunil Kumar Maharana", age="29", number=9114590459)
c.test()
