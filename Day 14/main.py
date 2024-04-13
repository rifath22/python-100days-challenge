from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

random_number = random.randint(0, len(data))


def format_data(random_number):
    one_item        = data[random_number]
    name            = one_item["name"]
    profession      = one_item["description"]
    country         = one_item["country"]
    follower_count  = one_item["follower_count"]
    input_data = f"{name}, a {profession}, from {country}"
    return input_data, follower_count

score = 0
game_continue = True
while game_continue:
    person1_input_data, person1_follower_count = format_data(random.randint(0, len(data)))
    person2_input_data, person2_follower_count = format_data(random.randint(0, len(data)))

    print(f"Compare A: {person1_input_data}")
    print(vs)
    print(f"Compare B: {person2_input_data}")
    
    users_choice = str(input("Who has more followers? Type 'A'  or 'B': ")).upper()

    if users_choice == "A":
        if person1_follower_count > person2_follower_count:
            score += 1
            clear()
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
    if users_choice == "B":
        if person1_follower_count < person2_follower_count:
            score += 1
            clear()
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False

print(f"Sorry, thats's wrong. Final score: {score}")
