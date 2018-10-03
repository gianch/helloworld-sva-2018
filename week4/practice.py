# for x in range(20):
# 	print (x)


global myVariable
myVariable = 0

def countUp(amount):
	global myVariable

	myVariable = myVariable + amount
	print(myVariable)
	countUp(5)

