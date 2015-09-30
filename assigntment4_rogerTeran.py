# Assignment 4

# Question 1

shannon_pangram = "squdgy fez, blank jimp crwth vox"
jock_pangram = "mr. jock, tv quiz phd, bags few lynx."

def code(char, pangram = None):
	if pangram is None:
		x = list("squdgy fez, blank jimp crwth vox")
		for item in x:
			if char == item:
				next_char = x[(x.index(item)+1)]
				if next_char == " ":
					next_char = x[(x.index(item)+2)]
					return print(next_char)
				elif next_char == "," or next_char == ".":
					next_char = x[(x.index(item)+3)]
					return print(next_char)
				else:
					return print(next_char)
		else:
			return print(char)
	else:
		x = list(pangram)
		for item in x:
			if char == item:
				next_char = x[(x.index(item)+1)]
				if next_char == " ":
					next_char = x[(x.index(item)+2)]
					return print(next_char)
				elif next_char == "," or next_char == ".":
					next_char = x[(x.index(item)+3)]
					return print(next_char)
				else:
					return print(next_char)
		else:
			return print(char)
		
# Calling the function
code('s')

# Question 2

def code_message(text_string, coding_function):
	new_message = ''
	for letter in text_string:
		if letter in coding_function:
			new_letter = coding_function[letter]
		else:
			new_letter = letter
		new_message += new_letter
	return print(new_message)

code = dict()
for num in range(97, 97+26):
    code[chr(num)] = chr(num-1)
code[' ']=' '

code_message("hello hal", code)
