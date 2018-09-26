# an object describing our player
player = { 
    "name": "p1", 
    "score": 0 ,
    "items": ""
    
}

paths = {
    "path1" : "hellish path",
    "path2" : "angelic path",
    "path3" : "an alternate path"
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

        print '------------------------------------------------------------------------'
        print '  __     ______  _    _ _____      _____      ___   __________    __    '
        print '  \ \   / / __ \| |  | |  __ \    |  __ \    / ^ \  |__  __|  |  |  |   '
        print '   \ \_/ / |  | | |  | | |__) |   | |__) |  / / \ \    | | |  |__|  |   '
        print '    \   /| |  | | |  | |  _  /    |  _  /  / /___\ \   | | |   __   |   '
        print '     | | | |__| | |__| | | \ \    | |     / /_____\ \  | | |  |  |  |   '
        print '     |_|  \____/ \____/|_|  \_\   |_|    /_/       \_\ |_| |__|  |__|   '
        print '                                                                        ' 
        print '----------------------------------------------------------------------- '
    if (name == "demon"):

        print '         ,  ,  , , ,      '
        print '        <(__)> | | |      '
        print '        | \/ | \_|_/      '
        print '        \-  -/   |        '
        print '        /\--/\  /|        '
        print '        \/  \/ / |        '
        
        
    if (name == "angel"):

        print '        -=-         ' 
        print '     (\  _  /)      '
        print '     ( \(")/ )      '
        print '     ( / ^ \ )      '
        print '      \\/ \//       '
        print '      /_____\       '     
        
        
    if (name == "sword"):

        print '     __     '
        print '     ||     ' 
        print '    _||_    '  
        print '   ( || )   '  
        print '     ||     '  
        print '     ||     '  
        print '     ||     ' 
        print '     ||     '  
        print '     ||     ' 
        print '     ||     ' 
        print '     ||     ' 
        print '     \/     '


def gameOver():

    print "-------------------------------"
    print "Oh No! Let Angel guide you back home."
    print "name: " + player["name"]
    print "score: " + str(player["score"])
    return 





def hellishPath():
    print "The path looks dark but you move forward anyway..."
    print "You stop when you notice something at on the path"
    printGraphic("demon")
    print "Oh No! A Demon!"
    
    pcmd = raw_input("choose fight or flight >")
    
    if (pcmd == "fight"):

        print "You perpare for combat if demon attacks"    
        print "You need to roll the power dice."
        raw_input("press enter >")
        difficulty = 8
        roll = rollDice(0, 20, difficulty)

        if (roll >= difficulty):

            print "You got it! You beat our first enemy"
            print "The second challenge begins"
            player["score"] += 50
            raw_input("press enter >")
            angelicPath()

        else:
            print "You don't have enough power. Try again"
            player["score"] -= 20
            hellishPath()
            
    if (pcmd == "flight"):
        
        print "Don't be a coward! This what makes a true adventurer "
        hellishPath()

def angelicPath():
    print "You walk down the second path, you notice something ahead on path"
    print "You come to see a Angel"
    printGraphic("angel")
    print "You need to roll the power dice to get pass"
    raw_input("press enter >")
    difficulty = 15
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):

        print "You got it! You won't have to worry about her getting in your way"
        print "The third challenge begins"
        player["score"] += 90
        raw_input("press enter >")
        secretPath()
        

    else:
        print "Uh-Oh she won't let you pass, she's too overprotective"
        player["score"] -= 10
        angelicPath()


def secretPath():
    print "You take the alternative route which bring you upon a cave."
    print "You see inside, you see something shiny in middle."
    print "You run over to se what it is, it a sword in a stone!"
    printGraphic("sword")
    print "You need to roll the power dice."
    raw_input("press enter >")
    difficulty = 15
    roll = rollDice(0, 20, difficulty)

    if (roll >= difficulty):

        print "You got it! You're a true adventurer! :D"
        player["score"] += 150
        gameOver()
        

    else:
        print "You don't have enough power. Try again"
        player["score"] -= 10
        secretPath()   




# BEGINNING 


def introGame():
    # let's introduce them to our world
    print "Welcome to YOUR PATH GAME. Before start. What is your name?"
    player["name"] = raw_input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print "Now is your turn " + player["name"] + "!"
    print "There are three paths leading to different directions,... "
    print "Each path will test your bravery, cunning and sense of direction"
    print "It's will be dangerous going alone!"
    print "And it will be a long but harrowing challenge."
    print "Are you ready?"

    pcmd = raw_input("choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print "You walk down the path, it leads into a three other paths"
        raw_input("press enter >")
        hellishPath()

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