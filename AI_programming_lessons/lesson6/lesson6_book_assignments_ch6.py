#book 6-1
emma_info = {
    "first_name": "Emma",
    "last_name": "Nielsen",
    "age": 24,
    "city": "Aalborg",
}
print(emma_info["first_name"])
print(emma_info["last_name"])
print(emma_info["age"])
print(emma_info["city"])

#book 6-2
fav_numbers = {
    "emma": "2",
    "nikolaj": "5",
    "rasmus": "3",
    "viktor": "4",
    "martin": "1",
}
for key, value in fav_numbers.items():
    print(f'{key.title()} has a favorite number and it is {fav_numbers[key]}')
# print(f'Emma has a favorite number and it is {fav_numbers["emma"]}')
# print(f'Nikolaj has a favorite number and it is {fav_numbers["nikolaj"]}')
# print(f'Rasmus has a favorite number and it is {fav_numbers["rasmus"]}')
# print(f'Viktor has a favorite number and it is {fav_numbers["viktor"]}')
# print(f'Martin has a favorite number and it is {fav_numbers["martin"]}')

#book 6-3
python_glossary = {
    "for": "Keyword used to create a loop",
    "if": "Keyword used to create a conditional statement",
    "return": "Keyword used to return a value to another place",
    "def": "Keyword used to create a new function",
    "while": "Keyword used to create a loop that runs until something isn't true anymore"
}
for key, value in python_glossary.items():
    print(f'{key}: {value}')

#book 6-4
#Naah fam i've done it

#book 6-5
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}
for key, value in rivers.items():
    print(f'{key.title()} runs through {value.title()}')
    print(key.title())
    print(value.title())

#6-6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',}

learners = ["sarah", "danni", "ruben", "adam"]

for learner in learners:
    if learner in favorite_languages.keys():
        print(f"Hello {learner.title()}, are you loving learning {favorite_languages[learner].title()}?")
    else:
        print(f"Hello {learner.title()}, what programming language is your favorite?;)")

#6-7
ruben_info = {
    "first_name": "ruben", 
    "last:name": "jensen", 
    "age": "21", 
    "city": "aalborg", 
}

adam_info = {
    "first_name": "adam", 
    "last:name": "møller", 
    "age": "21", 
    "city": "aalborg", 
}
people_info = [
    adam_info,
    ruben_info,
    emma_info
]
for person in people_info:
    print(f"{person}\n")

#6-8
bowie = {"animal": "dog", "race": "flatcoated_retriever", "owner": "nikolaj"}
nuka = {"animal": "dog", "race": "landseer", "owner": "august"}
findus = {"animal": "cat", "race": "forestcat", "owner": "dubrika"}
pets = [
    bowie,
    nuka,
    findus
]
for pet in pets:
    print(f"{pet}\n")

#6-9
favorite_places = {
    "aland": ["marroco", "gibralta", "china"],
    "xander": ["maldives", "india", "japan"],
    "lawrence": ["scotland", "england", "ireland"],
}
for person, places in favorite_places.items():
    print(f"{person} loves to visit all these places: {places}")

#6-10
favorite_numbers = {
    "victor": [1, 43, 9],
    "martin": [54, 83, 43],
    "john": [123, 456, 789],
}
for person, numbers in favorite_numbers.items():
    print(f"{person} has a lot of favorite numbers! Here they are: {numbers}")

#6-11
cities = {
    "aalborg": {
        "country": "denmark",
        "population": 211.684,
        "fact": "aalborg's biggest public attraction is the Zoo",
    },
    "viborg": {
        "country": "denmark",
        "population": 40.621,
        "fact": "viborg was the old old capital city of denmark",
    },
    "skagen": {
        "country": "denmark",
        "population": 7.547,
        "fact": "skagen is the northenmost city in denmark",
    }
}
for city, info in cities.items():
    print(f'{city} is located in {cities[city]["country"]}. The population is around {cities[city]["population"]} people,'
          f' and here is and interesting fact about {city}: {cities[city]["fact"]}')

#6-12
#no
