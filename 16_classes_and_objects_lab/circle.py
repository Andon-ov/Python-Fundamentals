# class Circle:
#     __pi = 3.14
#
#     def __init__(self,diameter):
#         self.diameter = diameter
#         self.radius = diameter/2
#
#     def calculate_circumference(self):
#         return 2 * self.__pi * self.radius
#     # returns the circumference of the circle
#
#     def calculate_area(self):
#         return circle.__pi * self.radius ** 2  # ** - на 2ра степен
#     # returns the area of the circle
#
#     def calculate_area_of_sector(self,angle):
#         return (angle/360) * self.__pi * self.radius ** 2
#     # gives the central angle in degrees, returns the area that fills the sector
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.r = diameter / 2

    def calculate_circumference(self):
        return (2 * circle.__pi) * self.r

    def calculate_area(self):
        return circle.__pi * self.r ** 2

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * circle.__pi * self.r ** 2


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
