j = 0
m = 1
n = -1
x = 2.5
y = 0.0

result = j and m
print(result)
print('----------')

result =  not (j or m)
print(result)
print('----------')

result =  not j or m
print(result)
print('----------')

result = not (not j and not m) 
print(result)
print('----------')

result = j <= 10 and x >= 1 and m
print(result)
print('----------')

result = not x or not n or m+n
print(result)
print('----------')

result = x * 5 and 5 or m / n
print(result)
print('----------')

result = (j==0) or x/j 
print(result)