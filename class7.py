inventory = [('widgets',100),('spam',30),('eggs',200)]
#Write a program that inputs the name of an item and reports the inventory level for that item
search_item = str(input('Which item are you looking for? '))

for item in inventory:
	if item[0] == search_item:
		print(item[1])

inventory = [('widgets',100),('spam',30),('eggs',200)]
#Write a program that inputs the name of an item and reports the inventory level for that item
#Assume there are lots of items in inventory. Stop the search when you've found the item in inventory
inventory = [('widgets',100),('spam',30),('eggs',200)]
search_item = str(input('Which item are you looking for? '))

for item in inventory:
	if item[0] == search_item:
		print(item[1])
		break				#break will automatically exit the loop >> useful when I'm searching for stuff

#In the same program, print a message if the item is not in inventory
inventory = [('widgets',100),('spam',30),('eggs',200)]
search_item = str(input('Which item are you looking for? '))

for item in inventory:
	if item[0] == search_item:
		print(item[1])
		break
else:
	print("Not found")			#WEEEEIRDDDDD

inventory = [('widgets',100),('spam',30),('eggs',200)]
reorder_level = [('widgets',80),('spam',32),('eggs',200)]
#Write a program that prints out the items that need to be reordered.
#Assume that the items may not be in the same order in the two lists

for item in inventory:
	name = item[0]
	for reord in reorder_level:
		if name == reord[0] and reord[1] >= item[1]:
			print("Buy", name)

inventory = [('widgets',100),('spam',30),('eggs',200)]
reorder_level = [('widgets',80),('spam',32),('eggs',200)]
reorder_quantity = [('widgets',300),('spam',400),('eggs',250)]
#Write a program that prints orders for each item that needs to be ordered
#For example: "Buy 400 spam"
#Assume that the items may not be in the same order in the three lists

for item in inventory:
	for reord in reorder_level:
		if item[0] == reord[0] and reord[1] >= item[1]:
			for qty in reorder_quantity:
				if item[0] == qty[0]:
					print("Buy", qty[1],"of",item[0])

inventory = [('widgets',100),('spam',30),('eggs',200)]
reorder_level = [('widgets',80),('spam',32),('eggs',200)]
reorder_quantity = [('widgets',300),('spam',400),('eggs',250)]
#Write a program that prints orders for each item that needs to be ordered
#For example: "Buy 400 spam"
#Assume that the items may not be in the same order in the three lists
#Since the lists may be long, insert breaks to make the program more efficient

for item in inventory:
	for reord in reorder_level:
		print(reord[0])
		if item[0] == reord[0]:
			if reord[1] >= item[1]:
				for qty in reorder_quantity:
					if item[0] == qty[0]:
						print("Buy", qty[1],"of",item[0])
						break
			break

inventory = [('widgets',100),('spam',30),('eggs',200)]
#Write a function find_item_quantity(name,a_list) that returns item quantity from a list of tuples like the inventory list
#   where name == first element of tuple
#Example: find_item_quantity('spam',inventory) should return 30

def find_item_quantity(name, a_list):
	for thing in a_list:
		if thing[0] == name:
			return thing[1]
	return 0

find_item_quantity('spam', inventory)

inventory = [('widgets',100),('spam',30),('eggs',200)]
reorder_level = [('widgets',80),('spam',32),('eggs',200)]
reorder_quantity = [('widgets',300),('spam',400),('eggs',250)]
#Write a program that prints orders for each item that needs to be ordered
#For example: "Buy 400 spam"
#Assume that the items may not be in the same order in the three lists

#Use the find_item_quantity function


#Problem: Extract the numbers from a string
#E.g.
#x is a string that contains the dollar values of inventory items
#Calculate the total dollar value of all items
x = 'widgets 3078.90 spam 432.78 eggs 10938.33'
y = x.split()
sum = 0
for index in range(1,len(y),2):
	sum += float(y[index])
print(sum)
# one possible solution
# for thing in x.split():
#     if thing is convertible into float
#     then it must be a float
    
# The problem is how do we know if it is convertible to float?
# If we try to convert something to float and it doesn't work, we get an exception
# An exception is an error from which the program cannot recover



























