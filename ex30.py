# set amount of people
people = 30
# declare amount of cars
cars = 40
# describe amount of trucks
trucks = 31


# evaluate if there are more cars than people or if there are less trucks than cars
if cars > people or trucks < cars:
    # say something smart
    print("We should take the cars.")
# if it isn't, check if there are less cars than people, do this
elif cars < people:
    # say something smart
    print("We should not take the cars.")
# if it isn't any of those, do this
else:
    # say something smart
    print("We can't decide.")

# check if there are more trucks than people
if trucks > cars:
    # say something smart
    print("That's too many trucks.")
# if it isn't, check if there are less trucks than cars, do this
elif trucks < cars:
    # say something smart
    print("Maybe we could take the trucks.")
# if it isn't any of those, do this
else:
    # say something smart
    print("We still can't decide.")

# check if there are more people than trucks
if people > trucks:
    # say something smart
    print("Alright, let's just take the trucks.")
# if it isn't, do this
else:
    # say something smart
    print("Fine, let's stay home then.")
