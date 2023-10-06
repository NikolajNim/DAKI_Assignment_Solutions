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

