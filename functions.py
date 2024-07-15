def areaOfACircle():
    radius = float(input("Input your radius: "))
    decimal_place = int(input("Input the number of decimal places for your result"))
    PIE = 3.142
    area = PIE * (radius ** 2)  #area of the circle
    if decimal_place:
        result = round(area,decimal_place)
    print(f"The area of the circle with radius {radius} is {area} ")

def placeholder():
    pass

# area1 = areaOfACircle()
# area2 = areaOfACircle()

def areaOfACircleWithReturnValue():
    radius = float(input("Input your radius: "))
    decimal_place = int(input("Input the number of decimal places for your result"))
    PIE = 3.142
    area = PIE * (radius ** 2)  #area of the circle
    if decimal_place:
        area = round(area,decimal_place)
    print(f"The area of the circle with radius {radius} is {area} ")
    return area

# area3 = areaOfACircleWithReturnValue()
# print(area3)

def area_of_circle(radius,decimal_place=4,convert_to_int=False):
    PIE = 3.142
    area = PIE * (radius ** 2)  #area of the circle
    if decimal_place:
        area = round(area,decimal_place)
    if convert_to_int == False:
        pass
    else:
        area = int(area)
    print(f"The area of the circle with radius {radius} is {area} ")
    return area
area4 = area_of_circle(9.7)