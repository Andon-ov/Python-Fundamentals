class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"

        elif self.price > money:
            return "Sorry, not enough money"

        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return f"Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)



# class Vehicle:
#     def __init__(self, vehicle_type, model, price):
#         self.vehicle_type = vehicle_type
#         self.model = model
#         self.price = price
#         self.owner = None
#
#     def buy(self, money: int, owner: str):
#         if money >= self.price and self.owner == None:
#             self.owner = owner
#             return f"Successfully bought a {self.vehicle_type}. Change: {money - self.price:.2f}"
#
#         elif money < self.price and self.owner == None:
#             return "Sorry, not enough money"
#         elif not self.owner == None:
#             return "Car already sold"
#
#     def sell(self):
#         if not self.owner == None:
#             self.owner = None
#         else:
#             return f"Vehicle has no owner"
#
#     def __repr__(self):
#         if not self.owner == None:
#             return f"{self.model} {self.vehicle_type} is owned by: {self.owner}"
#         else:
#             return f"{self.model} {self.vehicle_type} is on sale: {self.price}"
#
#
# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
