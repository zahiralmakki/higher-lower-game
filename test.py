# 100 Days of code
# Day 14 Project: Higher and Lower game 
# 1/3/2025

import random
# Show the game logo(art).
from art import logo, vs
from game_data import data


def format_data(account):
    """Format the account data into a printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
    
print(logo)
score = 0
game_should_continue = True
account_a = random.choice(data)
while game_should_continue:
    # Randomly generate account A info from the game data.
    
    account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for a guess.
    guess = input("Who has more followers 'A' or 'B': ").lower()

    # Check if user is correct.
    #### Get follower count for each account.
    #### Use if statement to check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Track the score.
    if is_correct:
        score += 1
        print(f"You're right, Current score is: {score}.")
        # Making account at position B became the next account at position A.
        account_a = account_b
    else:
        print(f"Sorry, that's wrong, Final score: {score}.")
        game_should_continue = False


