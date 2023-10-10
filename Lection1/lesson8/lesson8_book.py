# 9-1
from restaurant import Restaurant

restaurant = Restaurant("Tortilla_Flats", "Mexican")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant1 = Restaurant("Latinerly", "Classic fine dining")
restaurant2 = Restaurant("Sanwe", "Japanese")
restaurant3 = Restaurant("McDonalds", "Fastfood")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 9-3
class User:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user is called {self.first_name} {self.last_name},"
              f" and they are {self.age} years old, have a height of {self.height} cm")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! How are you today? ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Emma", "Nielsen", "24", "170")
user1.describe_user()
user1.greet_user()

user2 = User("Xander", "Schmidt", "21", "169")
user2.describe_user()
user2.greet_user()

user3 = User("Rasmus", "Nielsen", "25", "189")
user3.describe_user()
user3.greet_user()

user4 = User("Nikolaj", "Nim", "23", "183")
user4.describe_user()
user4.greet_user()

# 9-4
print(restaurant1.number_served)
restaurant1.number_served = 120
print(restaurant1.number_served)
restaurant1.set_number_served(162)
print(restaurant1.number_served)
restaurant1.increment_number_served(21)
print(restaurant1.number_served)

# 9-5
user5 = User("Victor", "Stentoft", 19, "201")
for i in range(10):
    user5.increment_login_attempts()
print(user5.login_attempts)
user5.reset_login_attempts()
print(user5.login_attempts)


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Nougat", "Caramel"]

    def display_flavors(self):
        print(f"These are all the available flavors: {self.flavors}")


ice_cream_stand = IceCreamStand("Den Blå Café", "Ice Cream")
ice_cream_stand.display_flavors()


# 9-7
class Admin(User):
    def __init__(self, first_name, last_name, age, height):
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()


# 9-8
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"An Admin has these privileges: {self.privileges}")


admin = Admin("Nikolaj", "Nim", 23, 183)
admin.privileges.show_privileges()


# 9-9
import car as car

new_car = car.ElectricCar("Tesla", "X", 2023)
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.get_range()
#9-10, 9-11 and 9-12
#done

#9-13
from die import Die
d6 = Die()
print("first d6")
for i in range(10):
    d6.roll_die()
d10 = Die(sides=10)
print("D10")
for i in range(10):
    d10.roll_die()
d20 = Die(sides=20)
print("d20")
for i in range(10):
    d20.roll_die()


