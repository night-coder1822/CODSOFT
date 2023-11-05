import random

def get_user_choice():
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    while user_choice not in ["r", "p", "s"]:
        print("Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
        user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        return "You win!"
        print()
    else:
        return "Computer wins!"
        print()

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your score: {user_score}, Computer's score: {computer_score}")

    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again != "y":
        break
