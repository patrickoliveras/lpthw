name = 'Zed A. Shaw'
age = 35 # not a lie
height_in = 74 # inches
height_cm = height_in * 2.54 # centimeters
weight_lbs = 180 # lbs
weight_kg = weight_lbs * 0.4535 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.");
