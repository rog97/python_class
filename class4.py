presidents = ["Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama"]
# How many presidents were named Bush?
number_named_bush = 0
for item in presidents: 
	if item == "Bush":
		number_named_bush += 1
print(number_named_bush)