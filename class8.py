try:
	k = float('hello')
except ValueError:
	print('Hey. k is not a number')
else:
	print(k)
print('After the try')


try:
	z = 5/0
	k = float('hello')
except ValueError:
	print('Hey. k is not a number')
except ZeroDivisionError:
	print("Dividing by zero...don't do that, bitch")
else:
	print(k)
print('After the try')

def add_nums_in_list(a_list):
	sum = 0
	try:
		for thing in a_list:
			try:
				sum += float(thing)
			except ValueError:
				continue
	except TypeError:
		return "Type Error"
	except:
		return "Unknown Error"
	return sum

x = "widgets 3078 paper clips 300.23 spam 432.78 cartons of eggs 10938.33"
add_nums_in_list(x)