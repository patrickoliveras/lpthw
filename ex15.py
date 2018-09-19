# include the argv module
from sys import argv

# get the filename argument from the command line
script, filename = argv

# get the text file
txt = open(filename)

# declare that you will be printing the files contents
print(f"Here's your file {filename}:")
# print the files content
print(txt.read())

txt.close()

# say that you'll be requesting the filename again
print("Type the filename again:")
# prompt for the filename
file_again = input("> ")

# retrieve the file again
txt_again = open(file_again);

# print it's content again
print(txt_again.read())

txt_again.close()
