# Assign the premise core to a variable
types_of_people = 10
# Inject premise core into general premise
x = f"There are {types_of_people} types of people."

# Assign punchline core part 1 to variable
binary = "binary"
# Assign punchline core part 2 to variable
do_not = "don't"
# Inject punchline cores into general punchline
y = f"Those who know {binary} and those who {do_not}."

# Deliver premise
print(x)
# Deliver punchline
print(y)

# Recall bad joke premise
print(f"I said: {x}")
# Recall bad joke punchline
print(f"I also said: '{y}'")

# Determine verdict
hilarious = False
# Build curveball
joke_evaluation = "Isn't that joke funny?! {}"

# Build criticism and drop it, no mercy
print(joke_evaluation.format(hilarious))

# Build non sequitor part 1 and assign it to variable
w = "This is the left side of..."
# Build non sequitor part 2 and assign it to variable
e = "a string with a right side."

# Combine and print
print(w + e)
