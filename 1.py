numbers = [x for x in range(1000)]
i = 0
try:
	while True:
		print(str(numbers[i]))
		i += 1
except IndexError:
	print("1000")
	print("It's the end son.")
	print("Go home")