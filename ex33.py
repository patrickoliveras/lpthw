numbers = []

def loop_it(limit, increment):
    i = 0
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

loop_it(10, 2)

print("The numbers: ")

for num in numbers:
    print(num)
