# we create a party of a function that takes in two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # show off cheese
    print(f"You have {cheese_count} cheeses!")
    # show off crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # show off that you are posh
    print("Man that's enough for a party!")
    # show off over all
    print("Get a blanket.\n")

print("we can just give the function numbers directly:")
# party with straight up numbers
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# party indirectly with cheese and cracker variables
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# party like a nerd
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# party like indirectly like a nerd
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
