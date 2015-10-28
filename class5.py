# x = ['a', 'b', 'c']
# for item in x:
# 	print(item)

# for boondoggle in range(0,len(x)):
# 	print(x[boondoggle])

# x = [101, 102, 103, 104, 100, 99]
# for something in range(2, len(x)):
# 	print(x[something] - x[something - 2])

x = ["France", "UK", "Mongolia", "UK", "Germany"]
for item in x:
	if item == "Mongolia":
		print("Yes")

print("--------------")

found = False
index = 0
while not found and len(x) > index:
	print(index)
	if x[index] == "Mongolia":
		found = True
	index += 1
if found:
	print("Yes")

# use while loop when you have a condition you want to get out of
print("--------------")

x = ["France", "UK", "UK", "Germany"]
found = False
for item in x:
	print(item)
	if item == "Mongolia":
		found = True
		break

print("--------------")

acc = 0
while True:
	x = int(input("A number (0 to end): "))
	if x == 0:
		break
	acc += x
print(acc)

# print("--------------")

# x = list(0)
# type(x)
# >> will return 'list'

print("--------------")

aa;ldkfjal;ksdjfa;lksdf = 1
blahhhh = 2
