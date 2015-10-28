class Base:
    def __init__(self,data=None):
        self.data='hello'

class Derived:
    def __init__(self,other=None):
        self.data='goodbye'
        if other:
            self.data=other.data


y=Base()
z=Derived(y)
x=Derived()
print(z.data,x.data)

# What will the following code print?
#
# class Base:
#     def __init__(self, data):
#         self.data1 = data
#
# class Derived(Base):
#     def __init__(self, data):
#         self.data2 = data
#
# x = Derived(1)
# print(x.data1, x.data2)

# What will be printed?

class Odd:
    def __init__(self,data):
        self.data=data

data='Bugs Bunny'

x=Odd('Tom and Jerry')
print(x.data)

# what will be printed?

class Animal:
    def number_legs(self):
        return 4

class Cat(Animal):

    pass

Whiskers = Cat()
print(Whiskers.number_legs())
