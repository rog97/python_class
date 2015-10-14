print("concatena"+"tion")

class SpecialString:
	
	def __init__(self,v):
		self.value=v
	
	def __eq__(self,other):
		if len(self.value) == len(other.value):
			return True
		else:
			return False
	
	def __lt__(self,other):
		if len(self.value) < len(other.value):
			return True
		else:
			return False

x = SpecialString('Hello')
y = SpecialString('Doctor')
print(x < y)

class SpecialString(str):	#str knows how to initialize itself since we are inheriting that behavior - can get rid of __init__
	
	def __lt__(self,other):
		if len(self) < len(other):	#no need for .value because the object str knows what the value is
			return True
		else:
			return False

x = SpecialString('Hello')
y = SpecialString('Doctor')
print(x < y)