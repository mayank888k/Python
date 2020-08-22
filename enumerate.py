lst=["Aaloo","Bhindi","Gajar","Mooli","Adrak"]
print(list(enumerate(lst)))

print()

for index, value in enumerate(lst):
    print(f"Vegetable {value} is at index {index} in Basket")

print()
for index, value in enumerate(lst,100):
    print(f"Vegetable {value} is at index {index} in Basket")

# Enumerate is used to get index of the iteration in a loop 
# You can change starting index accordingly as above
# Enumerate function make index and value a tuple