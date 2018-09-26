# an object describing our player
player = { 
    "name": "p1", 
    "score": 0
}


import random # random numbers
import sys # system stuff for exiting

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print "You roll a: " + str(result) + " out of " + str(maxNum)

    # if result <= difficulty:
    #     print "You don't have enough power to fight. Trying again...."
        
    #     raw_input("press enter >")
    #     rollDice(minNum, maxNum, difficulty)

    return result


def printGraphic(name):
    if (name == "title"):

        print '----------------------------------------------------------------'
        print ' __     ______  _    _ _____    _______ _    _ _____  _   _     '
        print ' \ \   / / __ \| |  | |  __ \  |__   __| |  | |  __ \| \ | |    '
        print '  \ \_/ / |  | | |  | | |__) |    | |  | |  | | |__) |  \| |    '
        print '   \   /| |  | | |  | |  _  /     | |  | |  | |  _  /| . ` |    '
        print '    | | | |__| | |__| | | \ \     | |  | |__| | | \ \| |\  |    '
        print '    |_|  \____/ \____/|_|  \_\    |_|   \____/|_|  \_\_| \_|    '
        print '                                                                '
        print '----------------------------------------------------------------'



                                                                                 


def gameOver():

    print "-------------------------------"
    print "Amazing! You did it"
    print "name: " + player["name"]
    print "score: " + str(player["score"])
    return 



def runGuns():
    print "You need to roll the power dice."
    raw_input("press enter >")
    difficulty = 8
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):

        print "You got it! You beat our first enemy"
        print "The second challenge begins"
        player["score"] += 50
        raw_input("press enter >")
        runTaxes()

    else:
        print "You don't have enough power. Try again"
        player["score"] -= 20
        runGuns()
        



def runTaxes():
    print "The second enemy is Taxes!"
    print "You need to roll the power dice to fight taxes."
    raw_input("press enter >")
    difficulty = 12
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):

        print "You got it! You won't pay more taxes"
        print "The third challenge begins"
        player["score"] += 90
        raw_input("press enter >")
        runPollution()
        

    else:
        print "You don't have enough power. Try again"
        player["score"] -= 10
        runTaxes()


def runPollution():
    print "The third enemy is Pollution!"
    print "You need to roll the power dice."
    raw_input("press enter >")
    difficulty = 15
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):

        print "You got it! We will live in better places"
        player["score"] += 150
        gameOver()
        

    else:
        print "You don't have enough power. Try again"
        player["score"] -= 10
        runPollution()   




# BEGINNING 


def introGame():
    # let's introduce them to our world
    print "Welcome to YOUR TURN GAME. Before start. What is your name?"
    player["name"] = raw_input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print "Now is your turn " + player["name"] + "!"
    print "Today you can do something against 3 common enemies in our society..."
    print "It will be a hard battle."
    print "Are you ready?"

    pcmd = raw_input("choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print "This is our first enemy to face. Guns!"
        raw_input("press enter >")
        runGuns()
    else:
        print "No? ... This is your opportunity to do something."
        pcmd = raw_input("press enter >")
        introGame() # repeat over and over until the player chooses yes!


# BEGINNING



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introGame() # start the intro

main() # this is the first thing that happens