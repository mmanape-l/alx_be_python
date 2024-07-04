# weather_advice.py

def get_clothing_recommendation(weather_condition):
    """
    Provides weather advice and clothing recommendations based on the weather condition.
    :param weather_condition: Current weather condition
    :return: Weather advice and clothing recommendation message
    """
    if weather_condition == "sunny":
        return f"It's sunny outside! {weather_condition.capitalize()} weather recommendation: Wear a t-shirt and sunglasses."
    elif weather_condition == "rainy":
        return f"It's rainy outside. {weather_condition.capitalize()} weather recommendation: Don't forget your umbrella and a raincoat."
    elif weather_condition == "cold":
        return f"It's cold outside. {weather_condition.capitalize()} weather recommendation: Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    # Define valid weather conditions
    valid_conditions = ["sunny", "rainy", "cold"]
    
    # Prompt the user for the current weather condition
    weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Validate user input
    while weather_condition not in valid_conditions:
        print("Invalid input. Please enter sunny, rainy, or cold.")
        weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Get weather advice and clothing recommendation based on weather condition
def get_clothing_recommendation(weather_condition):
    """
    Provides clothing recommendations based on the weather condition.
    :param weather_condition: Current weather condition
    :return: Clothing recommendation message
    """
    if weather_condition == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather_condition == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather_condition == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    # Define valid weather conditions
    valid_conditions = ["sunny", "rainy", "cold"]
    
    # Prompt the user for the current weather condition
    weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Validate user input
    while weather_condition not in valid_conditions:
        print("Invalid input. Please enter sunny, rainy, or cold.")
        weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Get clothing recommendation based on weather condition
    recommendation = get_clothing_recommendation(weather_condition)
    
    # Print the weather condition and clothing recommendation
    print(f"It's {weather_condition} weather today.")
    print(recommendation)

# Execute the main function when running the script
if __name__ == "__main__":
    main()