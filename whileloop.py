age = 50
while age > 18:
    print("you are an Adult")
    if age == 30:
        break
    age -= 10 #--age
print("You are a teenager")
#even number
for i in range(10):
    if i % 2 == 0:
        if i == 2:
            continue
        else:
            print(i)
