from random import randint
name = ""
for i in range(100):
	name = name + str(randint(0, 9))
name = name + ".txt"
try:
	f = open(name, "r")
	data = f.read()
	f.close()
except FileNotFoundError:
	print("This file no have")

