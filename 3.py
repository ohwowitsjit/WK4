while True:
	try:
		num = float(input("Enter your number: "))
		file = open("RATIONALS.txt", "a")
		file.write(str(num) +"\n")
		file.close()
	except:
		print("That ain't no rational mate! Go home and study man!")
		break
	
	