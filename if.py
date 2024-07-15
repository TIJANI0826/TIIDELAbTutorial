# age = int(input("Please type your age"))
# if age >= 80:
#     print("Very Old")
# elif age >=18:
#     print("Just Adult")
# else:
#     print("Teenager")

score = float(input("Please enter the score"))
#70 - 100 - A
if score > 100:
    print("Wrong")
elif score >= 70 and score <= 100:
    print("A")
elif (score >= 60) and (score < 70):
    print("B")
elif (score >= 50) and (score < 60):
    print("C")
elif (score >= 45) and (score <= 49):
    print("D")
elif (score >= 39) and (score < 45):
    print("E")
else:
    print("F")

