#list, dictionary, string, iterable
import string
alphabets = string.ascii_lowercase
print(alphabets)
list_alphabets = list(alphabets)
print(list_alphabets)

# for element in alphabets:
#     print(element.upper())
list_of_numbers_cube = [[1,1],[2,8],[3,27]]
# for item in list_alphabets:
#     print(item)
#     if item == "k":
#         print("You can now stop")
#         break
for i in list_of_numbers_cube:
    print(i[1])
    