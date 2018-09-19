from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

more_input = input("Gimme more. ")
print("Blarghh", more_input)
