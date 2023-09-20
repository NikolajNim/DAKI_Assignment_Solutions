#bog opgave 4-1
pizzas = ["pepe with drel", "Kebab and drel", "Chicken and drel"]
for pizza in pizzas:
    print(f"{pizza} is da best pizza")

print("I really love pizza. The best pizza i know is with kebab, chicken, onion and dressing in the oven."
      " If it can be really fancy, there should be cheese in the crust too")

#bog opgave 4-2
animals = ["goat", "cow", "sheep"]
for animal in animals:
    print(f"a {animal} animal have 4 legs")

print("As i said, all of these animals have 4 legs")

#bog opgave 4-3
for i in range(1, 21):
    print(i)

#bog opgave 4-4
million = []
for i in range(1, 1000001):
    million.append(i)
#print(million)

#bog opgave 4-5
print(min(million))
print(max(million))
print(sum(million))

#bog opgaver 4-6
numbers = []
for i in range(1, 20, 2):
    numbers.append(i)
print(numbers)

#bog opgave 4-7
numbers = []
for i in range(3, 30, 3):
    numbers.append(i)
print(numbers)

#bog opgave 4-8
numbers = []
for i in range(1, 11):
    numbers.append(i**3)
print(numbers)

#bog opgave 4-9
numbers = [i**3 for i in range(1, 11)]
print(numbers)

#bog opgave 4-10
print(f"The first 3 numbers in 'numbers' is: {numbers[:3]}")
print(f"The middle 3 numbers in numbers are: {numbers[3:6]}")
print(f"The last 3 numbers in numbers are: {numbers[7:]}")

#bog opgave 4-11
friend_pizzas = pizzas[:]
pizzas.append("pineapple pizza")
friend_pizzas.append("kiwi pizza")
for my_pizza in pizzas:
    print(f"My favorite pizzas are: {my_pizza}")
for my_friend_pizza in friend_pizzas:
    print(f"My friends favorite pizzas are: {my_friend_pizza}")

#bog opgave 4-12
#lmao ezpz

#bog opgave 4-13
basic_foods = ("hotdog", "burger", "pizza", "pie", "pita")

for food in basic_foods:
    print(food)
basic_foods = ("hotdog", "burger", "pizza", "salat:(", "veggies:(")
for food in basic_foods:
    print(food)

#bog opgave 4-14
#lmao??? t https://python.org/dev/peps/pep-0008

#bog opgave 4-15
#lmaoezpz