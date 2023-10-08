#book assignments
#8-1
def display_message():
    print("Hello, I have learned to write a function!")
display_message()

#8-2
def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book("Djævlens lærling")

#8-3 and 8-4
def make_shirt(text = "I Love Python", size = "L"):
    print(f"Here is a size {size} shirt with this text on the front: {text}")

make_shirt()
make_shirt(size="L")
make_shirt(size="XXXXL", text="MISTER FAT MAAAAAN")

#8-5
def describe_city(name, country="Denmark"):
    print(f"{name} is in {country}")

describe_city("Aalborg")
describe_city("Viborg")
describe_city("Paris", country="France")

#8-6
def city_country(city: str, country: str):
    formatted_message = f"{city.title()}, {country.title()}"
    return formatted_message

print(city_country("aalborg", "denmark"))
print(city_country("viborg", "denmark"))
print(city_country("tokyo", "japan"))

#8-7
def make_album(artist, album_title, number_of_songs=None):
    if number_of_songs:
        album = {
            "artist": artist,
            "album title": album_title,
            "number of songs": number_of_songs
        }
    else:
        album = {
            "artist": artist,
            "album title": album_title,
        }
    return album
album1 = make_album("KSI", "All Over The Place", number_of_songs=20)
print(album1)
album2 = make_album("Post Malone", "Hollywood's Bleeding")
print(album2)
album3 = make_album("The Longest Johns", "Smoke and Oakum", number_of_songs=10)
print(album3)

#8-8
# while True:
#     print("I can compile your favorite singer and their album! (type 'quit' to exit program)")
#     artist = input("What is the name of the artist? ")
#     album_name = input("What is the name of their album? ")
#     if artist == 'quit' or album_name == 'quit':
#         break
#     print(f" Here is the compilation: {make_album(artist, album_name)}")

#8-9 and 8-10 and 8-11
messages = [
    "Hello",
    "How",
    "Are",
    "you",
    "doing?"
]
def show_messages(messages):
    print(messages)

show_messages(messages)

def send_messages(messages):
    new_messages = []
    for message in messages:
        new_messages.append(message)
        print(message)
    return new_messages
new_list = send_messages(messages[:])
print(messages)
print(new_list)

#8-12
def sandwich(*args):
    print("You have ordered a sandwich with the following:")
    for arg in args:
        print(f"- {arg}")

sandwich("pepperoni", "ground beef", "salad", "Mushrooms", "pickles")
sandwich("milk", "cheese", "gouda", "parmachese")
sandwich("breed", "cum")

#8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Nikolaj', 'Nim',
 location='Aalborg',
 field='AI', occupation="Choir singer")
print(user_profile)

#8-14
def make_car(manufacturer, model, **kwargs):
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs

car = make_car("toyotaa", "Aygo", color="White", sky_window="Sky window")
print(car)