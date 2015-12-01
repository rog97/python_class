
# 1.A

x=[('2014-01-02',24.22),('2014-01-03',22.11),('2014-01-04',24.11)]
y=x
y[2]=('2014-01-04',24.21)
print(x[2])

# 1.B

x=[(1,[2,3],4)]
x[0][1][1]=4
print(x)

# 1.C

x={'a':1,'b':2}
x[89]='c'
print(x)

# 1.D

x="Hello"
print(x[-3:-1])

# 1.E

print(list(range(-6,6,2)))

# 1.F
"""
x='3'
y=2
print(x/y)
"""

# 1.G

z=[1,2,3,4]
x=[x**y for x in range(1,3) for y in z if x//2==0]
print(x)

# 1.H
"""
x = {1,4,5,2}
print(x[1])

set objects do not support indexing!
"""

# 1.I

x = [1,2,3]
y = x
y = [2,4]
print(x)

# 1.J

x = "Hello"
y = "Goodbye"
x, y = y, x
print(x, y)

# 1.K

print('spam'[1][0][0][0])

# Question 2

class Employee:

    def __init__(self, name, office, salary):
        self.name = name
        self.office_location = office
        self.salary = salary

    def totalComp(self):
        return self.salary

class Manager(Employee):

    def __init__(self, name, office, salary, bonus):
        Employee.__init__(self, name, office, salary)
        self.bonus = bonus

    def totalComp(self):
        return Employee.totalComp(self) * self.bonus/100 + Employee.totalComp(self)

    def __str__(self):
        return self.name

jill = Manager("Jill", "PH-A", 350000, 50)
print(jill)

# Question 3

def getCompositePosition(ticker, p1, p2):
    p1_pos = None
    p2_pos = None
    if ticker in p1:
        p1_pos = p1[ticker]
    if ticker in p2:
        p2_pos = p2[ticker]
    if p1_pos == None and p2_pos == None:
        return None
    if p1_pos == None:
        return p2_pos
    if p2_pos == None:
        return p1_pos
    return (p1_pos[0] + p2_pos[0], ((p1_pos[0]*p1_pos[1] + p2_pos[0]*p2_pos[1])/(p1_pos[0] + p2_pos[0])))

p1={'GOOG': (200, 324.11), 'GE': (800, 11.21), 'AAPL': (300, 21.22), 'TWTR': (450, 43.22)}
p2={'GOOG': (350, 217.11), 'ISIS': (400, 11.89), 'GE': (100, 32.11)}

print(getCompositePosition('GOOG', p1, p2))

# Question 4

def convertPort(portfolio_list):
    return_portfolio = dict()
    for element in portfolio_list:
        key = element[0]
        value = tuple((element[1], element[2], element[3]))
        return_portfolio[key] = value
    return return_portfolio

list_port=[('GOOG',200, 324.11,550.91), ('GE',800, 11.21,19.44),( 'AAPL',300, 21.22,107.11),
('TWTR',450, 43.22,37.88)]

print(convertPort(list_port))
