# price_dictionary = {
# 	"banana": 1.50,
# 	"avocado": 0.99,
# 	"heirloom tomato": 0.89,
# 	"cherry tomato pack": 3.00
#}

# Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.
bDayDict = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
}
print("Welcome to the birthday dictionary. We know the birthdays of: \n Albert Einstein \n Benjamin Franklin \n Ada Lovelace \n")

name = input("Who's brithday do you want to look up?")
if (name == "Albert Einstein"):
    print("Albert Einstein's birthday is " + bDayDict["Albert Einstein"])
elif (name =="Benjamin Franklin"):
    print("Benjamin Franklin's birthday is " + bDayDict["Benjamin Franklin"])
elif (name == "Ada Lovelace"):
    print("Ada Lovelace's birthday is " + bDayDict["Ada Lovelace"])
else:
    print("Sorry, that person is not known in this birthday dictionary.")
