
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
randomVIP = vips.pop(random.randint(0, len(vips)))
print(f"{randomVIP} won't be able to make it to the party:(")
vips.append("Adolf Hitler")

listsTheVIPS(vips)

#bog opgave 3-6



