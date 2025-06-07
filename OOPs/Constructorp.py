class Constructorp:
    def __init__(self):
        self.name = "Sunil Kumar Maharana"
        self.age = 29
        self.mob = 9114590459
        self.aadhar = 911655767004
        self.technology = "Python Automation Tester"

    def print_user(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile No:", self.mob)
        a = ""
        count = 0
        for i in str(c.aadhar):
            count += 1
            a += i
            if count == 4:
                a += " "
                count = 0
        print("Aadhar No:", a)
        print("Technology:", self.technology)


c = Constructorp()
c.print_user()
print(c.__dict__)
