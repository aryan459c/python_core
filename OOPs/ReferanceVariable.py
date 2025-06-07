class SalaryDetails:
    def __init__(self,name,userId,salary):
        self.name=name
        self.userId=userId
        self.salary=salary
    def User(self):
        print(f"User Name: {self.name}")
        print(f"User Id: {self.userId}")
        print(f"Salary : {self.salary}")

Salary=SalaryDetails("Sunil Kuamar Maharana","L14049002060",45000)
Salary.User()