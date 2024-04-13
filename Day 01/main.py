#1. Create a greeting for your program.
print("Welcome to the band name generator")
#2. Ask the user for the city that they grew up in.
city_name = str(input("Please give the city name you grew up in:\n"))
#3. Ask the user for the name of a pet.
pet_name = str(input("Please give the pet name you have:\n"))
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + pet_name
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print(f"Your band name is {band_name}")