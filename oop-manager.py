class Employee:
    raise_amnt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.a=first + '@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_riase(self):
        self.pay = int(self.pay * self.raise_amnt)
           

class Developer(Employee):  
    raise_amnt=1.08
    def __init__(self,first,last,pay,lan):
        super().__init__(first,last,pay)
        self.lan=lan

class manager(Employee):
    def __init__(self,first,last,pay,emps=None):
        super().__init__(first,last,pay)
        if emps is None:
            self.emps=[]
        else:
            self.emps=[]
            self.emps.append(emps)

    def add_emp(self,emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emp(self,emp):
        if emp in self.emps :
            self.emps.remove(emp)

    def print_emp(self):
        for emp in self.emps :
            return(f'----->{emp.fullname()}')
        


dev1 = Developer('mohamad','borghei',500,'python')
emp1 = Employee('hamid','tahami',400)
mgr1=manager('saeed','aghai',6000,dev1)

print(mgr1.first)
print(mgr1.pay)
mgr1.apply_riase()
print(mgr1.pay)
mgr1.add_emp(emp1)
#mgr1.print_emp()
print(mgr1.print_emp())
print()
mgr1.remove_emp(dev1)
#mgr1.print_emp()
print(mgr1.print_emp())


