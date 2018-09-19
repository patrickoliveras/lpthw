# enable argv, captain
from sys import argv

# Bring in the args!
script, input_file = argv

# lets make a funfunction for barfing out the whole file
def print_all(f):
    # BLARGHBLARGHBARF
    print(f.read())

# hold up
def rewind(f):
    # go back pls
    f.seek(0)

# now let's vomit in a controlled manner
def print_a_line(line_count, f):
    # say your line number, and push it out a little
    print(line_count, f.readline())

# now let's open a good ol file
current_file = open(input_file)

# announce total barf
print("First let's print the whole file: \n")
# let it out, all of it
print_all(current_file)

#announce something horrible
print("Now let's rewind, kind of like a tape.")

# bring it back in
rewind(current_file)

# announce mechanically controlled, non continuous barfing action
print("Let's print three lines:")

# start at the beginning. Please.
# value of current_line is 1
current_line = 1
# do a little
print_a_line(current_line, current_file)

# be conscious about how much has gone out and adjust
# value of current_line is 2
current_line += 1
# a little more
print_a_line(current_line, current_file)

# be conscious about how much has gone out and adjust
# value of current_line is 3
current_line += 1
# and a little bit more
print_a_line(current_line, current_file)
