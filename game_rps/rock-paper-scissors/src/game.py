import random

def get_user_choice():
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Enter a choice (rock, paper, scissors): ")
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "User wins!"
    return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(f"User chose {user_choice}. Computer chose {computer_choice}. {result}")

if __name__ == "__main__":
    play_game()