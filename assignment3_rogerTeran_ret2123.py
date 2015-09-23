# Assignment 3

# Problem 1

daily_sales = [('A', 150234.22), ('B', 73232.90), ('C', 110493.29), ('D', 231965.64), ('E', 66398.58)]
total_sales = 0

for sales in daily_sales:
	total_sales += sales[1]

average_sales = total_sales/len(daily_sales)

print('Total sales today: ' + '${:,.2f}'.format(total_sales))
print('Average sales today: ' + '${:,.2f}'.format(average_sales))

# Problem 2

daily_sales = [('A', 150234.22), ('B', 73232.90), ('C', 110493.29), ('D', 231965.64), ('E', 66398.58)]
budgeted_sales = [('A', 140296.00), ('B', 103981.00), ('C', 80452.00), ('D', 200900.00), ('E', 90000.00)]
performance_threshold = 20

for sales in daily_sales:
	for bsales in budgeted_sales:
		if sales[0] == bsales[0]:
			diff = ((sales[1]/bsales[1] - 1)) * 100
			if diff > performance_threshold:
				print("Store " + sales[0] + " overperformed its budget")
			else:
				print("Store " + sales[0] + " underperformed its budget")
