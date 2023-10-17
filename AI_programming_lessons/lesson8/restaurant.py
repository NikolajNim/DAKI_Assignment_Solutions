class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant is called {self.name} and the cuisine served here is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num