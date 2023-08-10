class person:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        #getter
        print('getting name')
        return self.__name
    
    @name.setter
    def name(self,value):
        #setter
        print(f'setting name to {value}')
        self.__name = value

    @name.deleter
    def name(self):
        print('deleting name')
        del self.__name

p=person('mohamad')
print(f'the name is {p.name}')
print()
p.name = 'sara'
print(f'the name is {p.name}')
del p.name