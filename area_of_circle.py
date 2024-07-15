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

area2 = area_of_circle(4.5)
print(area2)

