# Set template
formatter = "{} {} {} {}"

# Inject numbers into template using format function
print(formatter.format(1, 2, 3, 4))
# Inject spelled out numbers into template using format function
print(formatter.format("one", "two", "three", "four"))
# Inject booleans into template using format function
print(formatter.format(True, False, False, True))
# Inject template into template using format function
print(formatter.format(formatter, formatter, formatter, formatter))
# Inject strings into template using format function, one string per line
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
