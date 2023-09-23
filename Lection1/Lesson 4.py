#bog opgave 5-1
fav_pizza_topping = "kebab"
print("Is my favorite pizza topping == kebab? I predict True")
print(fav_pizza_topping == "kebab")
print("Is my favorite pizzatopping == achovies?? I dont think so fister medister")
print(fav_pizza_topping == "anchovies")
have_tattoo = "No"
print("hmm do i have a tattoo? I think that is a false statement")
print(have_tattoo == "Yes")
want_tattoo = "yes"
print("But do i want a tattoo? I predict True")
print(want_tattoo == "yes")
fav_videogame = "Assassin's Creed"
print("Is my favorite videogame == Assassin's Creed? I predict true")
print(fav_videogame == "Assassin's Creed")

#bog opgave 5-2
print("Suuh dude" == "Sup Homie")
print("wassup ma ni" == "wassup ma ni")

print("abriham lincon".title() == "ABRIHAM LINCON".title())
print("Adolf lincler".lower() == "ADolf Hitlaer".lower())

print(1==1)
print(0==1)
print(1<2)
print(2<1)
print(1>2)
print(2>1)
print(4<=1)
print(4<=4)
print(5>=2)
print(5>=6)

print(1==1 and 2==2)
print(1==3 and 2==2)

numbers = [1,2,3,4,5,6,7,8,9]
print(3 in numbers)
print(10 in numbers)

#bog opgave 5-3
alien_color = "green"
if alien_color == "green":
    print("You have scored 5 points!")
if alien_color == "red":
    print("You have scored 5 points!")

#bog opgave 5-4
alien_color = "green"
if alien_color == "green":
    print("You have scored 5 points!")
else:
    print("You have earned 10 points!")

alien_color = "red"
if alien_color == "green":
    print("You have scored 5 points!")
else:
    print("You have earned 10 points!")

#bog opgave 5-5
alien_color = "green"
if alien_color == "green":
    print("You have scored 5 points!")
elif alien_color == "red":
    print("You have earned 10 points!")
else:
    print("you have scored 15 points! OMEGAHOT")

alien_color = "red"
if alien_color == "green":
    print("You have scored 5 points!")
elif alien_color == "red":
    print("You have earned 10 points!")
else:
    print("you have scored 15 points! OMEGAHOT")


alien_color = "yellow"
if alien_color == "green":
    print("You have scored 5 points!")
elif alien_color == "red":
    print("You have earned 10 points!")
else:
    print("you have scored 15 points! OMEGAHOT")


#bog opgave 5-6
age = 2
if age < 2:
    print("gugugaga")
elif age >= 2 and age <4:
    print("uwu u a good booiii Toddler")
elif age >= 4 and age < 13:
    print("wassup kid?")
elif age >= 13 and age < 20:
    print("Why u gotta be like dis u teenager filth")
elif age >= 20 and age < 65:
    print("U a real man now homie adult")
else:
    print("WAssuo master elder person idk")

#bog opgave 5-7
favorite_fruits = ["apples", "Oranges", "peaches"]
if "kiwi" in favorite_fruits:
    print("eww nah its good")
if "apples" in favorite_fruits:
    print("They gotta be crunchy")
if "peaches" in favorite_fruits:
    print("I love peaches")
if "bananas" in favorite_fruits:
    print("I like you but naaah")
if "Oranges" in favorite_fruits:
    print("Probs the best citrus fruit")
