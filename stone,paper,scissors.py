import random
#speaking with the help of external module just copied from google
import pyttsx3
engine = pyttsx3.init()
engine.say("welcome to game lets play ")
engine.runAndWait()
count = int(input("Enter the number of times you want to play the game: "))
for i in range(count):
    options = ["stone", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    if computer_choice == user_choice:
        print(f"your choice= {user_choice} & computer choice= {computer_choice}")
        print("It's a draw!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print(f"your choice= {user_choice} & computer choice= {computer_choice}")
        print("You win!")
    else:
        print("Oops! You lost.")
