import random
#bog opgave 2-1 og 2-2
massage = "Lmao"
print(massage)

massage = "OmegaLmao"
print(massage)

#bog opgave 2-3
person_name = "Xander smith"
message = f"Hello {person_name}, do you  find it fun to learn Python?:) "
print(message)

#bog opgave 2-4
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

#bog opgave 2-5 og 2-6
famous_quote = "\"I did not have sexual relations with that woman.\""
famous_person = "Bill Clinton"
message = f"{famous_quote} - {famous_person}"
print(message)

#bog opgave 2-7
person_name = "\n Nikolaj "
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

#bog opgave 2-8
my_website = "https://www.omegalul.com"
print(my_website.removeprefix("https://"))
my_file = "homework.dontlook"
print(my_file.removesuffix(".dontlook"))


#bog opgave 2-9
#Prints 4 different equations equal to 8
print(4+4)
print(12-4)
print(4*2)
print(16/2)

#bog opgave 2-10
#creation and printing of my favorite number
fav_number = 5
message = f"My favorite number is {fav_number}!"
print(message)

#bog opgave 2-11
#Done!

#bog opgave 2-12
import this

#bog opgave 3-1
friends = ["Xander", "Anton", "Rasmus", "Ayush", "Aland"]
for i in range(len(friends)):
    print(friends[i])


#bog opgave 3-2
for i in range(len(friends)):
    message = f"Hello {friends[i]}, you're funny lol"
    print(message)

#bog opgave 3-3
transport = ["Lambo", "Harley", "Corvette", "Azzam", "Roman Abramovich's Boeing"]
for i in range(len(transport)):
    message = f"{transport[i]} is an awesome vehicle"
    print(message)

#bog opgave 3-4
vips = ["Albert Einstein", "Steven Hawking", "Barack Obama", "Bente Broder Jørgensen", "Matt Mercer"]
print(vips)

def listsTheVIPS(vips):
    for i in range(len(vips)):
        message = f"Hello {vips[i]}, I would like to invite you to my dinner party! It takes place at my mansion Friday The 13th of October"
        print(message)

listsTheVIPS(vips)
print(vips)
#bog opgave 3-5
randomVIP = vips.pop(random.randint(0, len(vips)-1))
print(f"{randomVIP} won't be able to make it to the party:(")
vips.append("Adolf Hitler")

listsTheVIPS(vips)

#bog opgave 3-6
message = "I just found a bigger table, let's invite some more people!"
print(message)
new_person1, new_person2, new_person3 = "Xander Smith", "Bolette", "William"
vips.insert(0, new_person1)
vips.insert(3, new_person2)
vips.append(new_person3)
print(vips)
listsTheVIPS(vips)

#bog opgave 3-7
message = "Unfortunately, I can only invite 2 people to the party:("
print(message)
for i in range(len(vips)):
    if len(vips) > 2:
        popped_person = vips.pop(-1)
        print(f"Sorry {popped_person}, I wont be able to have you to the party:((")

listsTheVIPS(vips)

del vips[-1]
del vips[-1]
print(vips)
del vips


#bog opgaver 3-8
places = ["Malaga", "Paris", "Bahamas", "Aalborg", "Arsenal"]
print(places)
print(sorted(places))

print(places)
print(sorted(places, reverse=True))

print(places)
places.reverse()

print(places)
places.reverse()

print(places)
places.sort()

print(places)
places.sort(reverse=True)
print(places)

#bog opgaver 3-9
vips = ["Albert Einstein", "Steven Hawking", "Barack Obama", "Bente Broder Jørgensen", "Matt Mercer"]
message = f"I have invited {len(vips)} people to the party"
print(message)

#bog opgaver 3-10
mountains = ["Mount Everest", "Kilimanjaro", "Himalaya", "Godwin Austen", "Kangchenjunga"]
rivers = ["The Nile", "The Amazon", "The Mississippi", "The Yellow", "The Yangtze"]
countries = ["Spain", "France", "Denmark", "Germany", "Japan"]
languages = ["German", "Spanish", "French", "Danish", "Japanese"]
print(mountains)
print(rivers)
print(countries)
print(languages)

random_country = countries.pop(random.randint(0, len(countries)-1))
print(countries)
countries.append("Finland")
print(countries)
languages.insert(4, "Latin")
print(languages)
popped_river = rivers.pop(-1)
print(f"get of here {popped_river}")
del mountains[-1]
print(mountains)
del rivers
languages.clear()
print(languages)



