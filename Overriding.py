class Employee:

    apply_raise=1.5

    def __init__(self,first,last,empid,pay):

        self.first=first

        self.last=last

        self.empid=empid

        self.pay=int(pay)

    def display(self):

        print("first name: ", self.first)

        print("last name: ", self.last)

        print("empid: ",self.empid)

        print("pay: ", self.pay)

    def pay_raise(self):

        self.pay=int(self.pay)*self.apply_raise

class Developer(Employee):

    apply_raise=2.5

    def __init___(self,first,last,empid,pay):

        super().__init__(first,last,empid,pay)

    def pay_raise(self):

        self.pay=int(self.pay)*self.apply_raise

class Manager(Employee):

    apply_raise=3.5

    def __init___(self,first,last,empid,pay):

        super().__init__(first,last,empid,pay)

    def pay_raise(self):

        self.pay=int(self.pay)*self.apply_raise

e1=Employee("akash","dallen","101",10000)

print(e1.pay)

e2=Developer("nagendra","herle","102",10000)

print(e2.pay)

e3=Manager("vaibhav","hatwar","103",10000)

print(e3.pay)

e1.pay_raise()

e2.pay_raise()

e3.pay_raise()

e1.display()

e2.display()

e3.display()
