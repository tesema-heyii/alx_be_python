# weather_advice.py

# Prompt the user for the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on the user's input
if weather.lower() == "sunny":
    # If the weather is sunny, recommend light clothing
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    # If the weather is rainy, recommend waterproof gear
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    # If the weather is cold, recommend warm clothing
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handle any other input that is not sunny, rainy, or cold
    print("Sorry, I don't have recommendations for this weather.")
