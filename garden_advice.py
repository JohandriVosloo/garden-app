# Ask the user to enter the current season.
# input() pauses the program and waits for the user to type something.
# strip() removes any accidental spaces before or after the input.
# lower() converts the input to lowercase so comparisons work reliably.
season = input("Enter the season (e.g. summer, winter): ").strip().lower()

# Ask the user to enter the type of plant.
# The same cleaning steps are applied to ensure consistent input.
plant_type = input("Enter the plant type (e.g. flower, vegetable): ").strip().lower()

# Create an empty string variable to store the gardening advice.
# Advice will be added to this variable as conditions are checked.
advice = ""

# Check which season the user entered and add appropriate advice.
# The if statement runs only if the condition is true.
if season == "summer":
    # If the season is summer, add summer-specific advice.
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    # If the season is winter, add winter-specific advice.
    advice += "Protect your plants from frost with covers.\n"
else:
    # If the season is not recognised, provide a default message.
    advice += "No advice for this season.\n"

# Check the plant type and add additional advice based on it.
if plant_type == "flower":
    # Advice specific to flowers.
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    # Advice specific to vegetables.
    advice += "Keep an eye out for pests!"
else:
    # Default advice if the plant type is not recognised.
    advice += "No advice for this type of plant."

# Output the final combined advice to the user.
# print() displays the contents of the advice variable on the screen.
print(advice)
