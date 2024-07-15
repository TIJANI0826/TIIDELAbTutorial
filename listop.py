import string
fruits = ["banana", "orange", "pawpaw", "strawberry"]
uppercase_alphabet = list(string.ascii_letters)
print(uppercase_alphabet)
print(fruits[1])

#adding a list to another

vegetbales = ["cabbage", "melon", "watermellon"]

fruit_veg = fruits + vegetbales
print(fruit_veg)

fruit_veg[3] = "Strawberry"
fruit_veg.append("Apple")
fruit_veg.append("Mango")
print(fruit_veg)
print(fruit_veg.pop())
print(fruit_veg)
print(fruit_veg.pop(2))
print(fruit_veg)
del fruit_veg[4]
print(fruit_veg)
fruit_veg.insert(2,"Cashew")
print(fruit_veg)
fruit_veg.remove("cabbage")
print(fruit_veg)
fruit_veg_reverse = reversed(fruit_veg)
print(fruit_veg_reverse)
#list comprehension
uppercase_fruit_veg = [item.upper() for item in fruit_veg_reverse]
print(uppercase_fruit_veg)
print(sorted(uppercase_fruit_veg))

for item in fruit_veg:
    print(item)

print(fruit_veg[1:4]) #last index is not include
print(fruit_veg[-1])
print(fruit_veg[:4])#last index is not include