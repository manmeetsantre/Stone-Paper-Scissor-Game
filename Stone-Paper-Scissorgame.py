import random

def game():
    print("Are you bored...? Then, come on let's play Stone-Paper-Scissors Game!\n")
    print("""Rules of the game are as follows: 
          o Type 'Stone', 'Paper', or 'Scissors' to play, or 'Exit' to end the game.  
          o Stone beats Scissors, Scissors beats Paper, Paper beats Stone.\n""")

    options = ["Stone", "Paper", "Scissors"]
    #initializing inital points of both to 0
    user_points = 0
    computer_points = 0
    #Using conditional statements
    while True:

        user_choice = input("Your choice (Stone, Paper, Scissors): ").capitalize()

        if user_choice == "Exit":
            break

        if user_choice not in options:
            print("Invalid choice. Please choose Stone, Paper, or Scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a Tie!")
        elif (user_choice == "Stone" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Stone"):
            print("You Win this round!")
            user_points += 1
        else:
            print("Computer Wins this round!")
            computer_points += 1

        print(f"Score: You - {user_points}, Computer - {computer_points}\n")

    print("\nGame Over!")
    print(f"Final Scores: You - {user_points}, Computer - {computer_points}")
    if user_points > computer_points:
        print("Congratulations! You won!")
    elif user_points < computer_points:
        print("Better luck next time! The computer won.")
    else:
        print("It's a tie! You may play again.")

game()
