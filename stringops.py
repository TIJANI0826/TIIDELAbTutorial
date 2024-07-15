import string
first_name = "Ibrahim"
last_name = 'Tijani'
#String indexing
print(first_name[2])
print(first_name[-3])
#concatenation 
fullname = first_name + " " + last_name
print(fullname)

#slicing
print(first_name[2:4]) #
print(first_name[-3:-1])

sentence = 'it\'s a Tuesday'
sentence2 = """
        it' a Tuesday,
        We are going to a party.
"""
age = 20
print(sentence2)
print(f'I am {first_name}, {last_name}. I am {age} years old')
print("I am %s, %s. I am %d years old'" % (last_name,last_name,age))
print("I am {}, {}. I am {} years old".format(first_name,last_name,age))
#upppercase
print(first_name.upper())
print(first_name.lower())

print(string.ascii_uppercase)