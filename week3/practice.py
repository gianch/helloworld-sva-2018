theLocation = "classroom"
myLocation = "outside"

if(myLocation != theLocation):
	print("a winner is you!!")

# "is" is the same than == 


# ++  =  +1   --  = -1
 

myMonies = 5
costOfThing = 6

if (myMonies >= costOfThing):
	print ("you have enough")
else: 
	print ("you don't have enough")



def sayHello():
	print("hello world")

def sayGoodbye():
	print("goodbye cruel world")

mood = "happy"

if (mood == "happy"):
	sayHello()
else:
	sayGoodbye()


# def saySomething(something)
# 	print(something)

# saySomething("hello world")


def testLocation(location):
	if (location == "gate"):
		return "ask for key"
	else:
		return "not sure what to do here"

sayToPlayer = testLocation("gate")

print(sayToPlayer)