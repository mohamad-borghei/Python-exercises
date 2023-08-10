class employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname
       
    @property
    def email(self):
        return self.fname + self.lname + '@gmail.com'
    
    @property
    def fullname(self):
        if self.fname is not None:
          return self.fname + self.lname 
        else:
           return 'There is no name'
    
    @fullname.setter
    def fullname(self,value):
        if value is not None:
            fname , lname = value.split(' ')
            self.fname=fname 
            self.lname= lname 
        else:
            print('There is no name')
        

    @fullname.deleter
    def fullname(self):
        print('name deleted')
        self.fname=None
        self.lname=None
    
emp1=employee('mohamad','borghei')
emp1.fullname='amiri moini'
print(emp1.fname)
print(emp1.lname)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)