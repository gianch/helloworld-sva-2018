# let the user know what's going on
print ("Do you want to know your future?")
print ("Answer the questions below to discover it.")
print ("-----------------------------------")

# variables containing all of your story info
day = raw_input("Enter your favorite day of the week: ")
number = raw_input("A number between 4 and 10: ")
location1 = raw_input("Name a country: ")
location2 = raw_input("Name another country: ")
president = raw_input("A current president of any country that you don't like: ")
person = raw_input("A living person that you admire: ")
activity = raw_input("A activity that you like to do for fun (verb + noun): ")
profession = raw_input("A profession that you wanted to do when you were a kid: ")
adjective = raw_input("Name a adjective: ")


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "A " + day + " within " + number + " years, you will plan to travell to " + location1 + " but the plane will be hijacked by " + president + "." \
" As one of the demands, the airplane will land in " + location2 + ". There you will meet " + person + " who will ask you to " + activity + " together. " \
" Suddenly, a " + profession + " will come up and hire you both to work for a project. It will be the beggining of your " + adjective + " career." 
# finally we print the story
print (story)
