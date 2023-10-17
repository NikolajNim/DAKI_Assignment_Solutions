#7-1
# message = input("What kind of car would you like for your rental? ")
# print(f"Here is the {message} you were looking for!")

#7-2
# question = int(input("Hello, welcome to tortilla flats! How many pwoplw are you this evening? "))
# if question > 8:
#     print("Sorry, we don't have a table big enough for you yet. You will have to wait")
# else:
#     print("We have a table for you right over here!")

#7-3
# question = int(input("Write a number, and i will tell you, if it is a multiple of 10! "))
# if question % 10 == 0:
#     print(f"{question} is a multiple of 10!")
# else:
#     print(f"{question} is not a multiple of 10:(")

#7-4
# requested_pizza_toppings = []
# while True:
#     question = input("What would you like on you pizza? (Enter 'quit' to confirm order): ")
#     if question == "quit":
#         print(f"Here is your pizza with {requested_pizza_toppings}!")
#         break
#     else:
#         requested_pizza_toppings.append(question)
#         print(f"{question} has been added to your pizza!")

#7-5
# while True:
#     question = int(input("Hello, what is your age? "))
#     age = question
#     if age < 3:
#         print("Your ticket is free!")
#     elif 3 <= age <= 12:
#         print("Your ticket costs $10;)")
#     else:
#         print("Your ticket costs $15:)")

#7-6
#suck me

#7-7
# while True:
#     print("lmao")

#7-8 and 7-9
# sandwich_orders = [
#     "chicken and bacon sandwich",
#     "pastrami sandwich",
#     "eggsalad sandwich",
#     "monte cristo sandwich",
#     "pastrami sandwich",
#     "meatball sandwich",
#     "pastrami sandwich",
#     "sloppy joe",
# ]
# finished_sandwich_orders = []
# for sandwich in list(sandwich_orders):
#     if sandwich == "pastrami sandwich":
#         print(f"The deli has run out of {sandwich}s. order a new")
#         sandwich_orders.remove(sandwich)
#     else:
#         print(f"Your {sandwich} was made, Enjoy!")
#         finished_sandwich_orders.append(sandwich)
#         sandwich_orders.remove(sandwich)
# print(f"All of these sandwiches was made: {finished_sandwich_orders}")

#7-10
dream_vacations = []

run_flag = True
while run_flag:
    question = input("Where is your dream vacation? ")
    if question == "end poll":
        run_flag = False
    dream_vacations.append(question)
print(f"The dream vacations of the poeple are: {dream_vacations}")



