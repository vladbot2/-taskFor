import random

greetings = ["Hello!", "Good day!", "Hi!", "Hey!", "Nice to see you!"]
farewells = ["See you later!", "Goodbye!", "Take care!", "Farewell!", "All the best!"]

def handleGreeting():
    return random.choice(greetings)

def handleFarewell():
    return random.choice(farewells)

def handleRandomImage(category):
    imageCategories = {
        "nature": ["", "nature2.jpg", "nature3.jpg"],
        "animals": ["animal1.jpg", "animal2.jpg", "animal3.jpg"],
        "cars": ["car1.jpg", "car2.jpg", "car3.jpg"]
    }
    
    if category not in imageCategories:
        return f"Category '{category}' not found. Please try another one."
    
    return random.choice(imageCategories[category])

print(handleGreeting())
print(handleFarewell())
print(handleRandomImage("nature"))
print(handleRandomImage("music"))
