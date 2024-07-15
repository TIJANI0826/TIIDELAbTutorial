phonebook = {
    'name' : "Ibrahim",
    'phone_number' : "08141994147",
    "email" : "ibrahimtijani08@gmail.com"
}

phonebook2 = dict(name="Ibrahim", phone_number="08141994147",
                  email="ibrahimtijani08@gmail.com")
print(phonebook)
print(phonebook2)
phonebook['name'] = "Ibrahim Tijani"
phonebook['phone_number'] = "0812344590"

#del phonebook["email"]
#phonebook.pop("email")
phonebook.popitem()
phonebook2.clear()
print(phonebook)
print(phonebook2)
print(phonebook.values())
print(phonebook.items())
print(phonebook.keys())
print(list(range(0,10))) #creates an iterator of numbers with start and end
cubes_of_1_to_10 = {x: x**3 for x in range(0,10)}
print(cubes_of_1_to_10)

phonebook3 = {
    "one": {
    'name' : "Ibrahim",
    'phone_number' : "08141994147",
    "email" : "ibrahimtijani08@gmail.com"
    },
    "two": {
    'name' : "Tijani",
    'phone_number' : "0811223344",
    "email" : "abc@gmail.com"
    }
}

print(phonebook3)