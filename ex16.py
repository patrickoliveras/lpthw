# bring in the sweet argv functionality
from sys import argv

# retrieve filename from command line
script, filename = argv

# Give instructions on how to be careful
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Pause for confirmation
input("?")

# inform about opening action
print("Opening the file...")
# open file in write mode
target = open(filename, 'w')

# inform about subsequent truncation
print("Truncating the file. Goodbye!")
# truncate that mf
target.truncate()

# inform about requiring for three strings
print("Now I'm going to ask you for three lines.")

# ask for three hits
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# inform about writing to file those sentences
print("I'm going to write these to the file.")

#
target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we close it.")
target.close()
