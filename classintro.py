class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def print_brand(self):
        print("The brand of the car is %s" % self.brand)
    def car_model(self):
        print("The model is %s " % self.model)
    def __str__(self):
        return f"The is {self.brand} {self.model}"

car_1 = Car("Toyota", "Camry")
car_1.print_brand()

car_2 = Car("Mazda", "406")
car_2.print_brand()
car_2.car_model()

car_3 = Car("BMW", "Youtube 1.0")
car_3
print(car_3)