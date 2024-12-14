import random

def game():
    print("Are you bored...? Then, come on let's play Stone-Paper-Scissors Game!\n")
    print("""Rules of the game are as follows: 
          o Type 'Stone', 'Paper', or 'Scissors' to play, or 'Exit' to end the game.  
          o Stone beats Scissors, Scissors beats Paper, Paper beats Stone.\n""")

    options = ["Stone", "Paper", "Scissors"]
    #initializing inital points of both to 0
    user_points = 0
    cpu_points = 0
    #Using conditional statements
    while True:

        user_choice = input("Your choice (Stone, Paper, Scissors): ").capitalize()

        if user_choice == "Exit":
            break

        if user_choice not in options:
            print("Invalid choice. Please choose Stone, Paper, or Scissors.")
            continue

        cpu_choice = random.choice(options)
        print(f"CPU chose: {cpu_choice}")

        if user_choice == cpu_choice:
            print("It's a Tie!")
        elif (user_choice == "Stone" and cpu_choice == "Scissors") or \
             (user_choice == "Scissors" and cpu_choice == "Paper") or \
             (user_choice == "Paper" and cpu_choice == "Stone"):
            print("You Won this round!")
            user_points += 1
        else:
            print("CPU Won this round!")
            cpu_points += 1

        print(f"Points: You - {user_points}, CPU - {cpu_points}\n")

    print("\nGame Over!")
    print(f"Final Points: You - {user_points}, CPU - {cpu_points}")
    if user_points > cpu_points:
        print("Congratulations! You won!")
    elif user_points < cpu_points:
        print("Better luck next time! The cpu won.")
    else:
        print("It's a tie! You may play again.")

game()
