file = open("WORDS.txt", "r")
largest_string = ""
largest_freq = 0

for line in file:
	try:
		num = int(line.strip())
		if num > largest_freq:
			largest_string = current_string
			largest_freq = num
	except ValueError:
		current_string = line.strip()
file.close()
print(" The code with the highest occurences is " + largest_string + " with " + str(largest_freq) + " occurences")