import random

def stone_paper_scissors():
    print("Let's play Stone-Paper-Scissors Game!\n")
    print("""Rules for playing the game: 
            Stone beats Scissors, Scissors beats Paper, Paper beats Stone.""")
    print("            Type 'Stone', 'Paper', or 'Scissors' to play, or 'Exit' to quit.\n")

    options = ["Stone", "Paper", "Scissors"]
    player_score = 0
    computer_score = 0

    while True:
        # Get player's choice
        player_choice = input("Your choice (Stone, Paper, Scissors): ").capitalize()

        # Exit condition
        if player_choice == "Exit":
            break

        # Validate input
        if player_choice not in options:
            print("Invalid choice. Please choose Stone, Paper, or Scissors.")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a Tie!")
        elif (player_choice == "Stone" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Stone"):
            print("You Win this round!")
            player_score += 1
        else:
            print("Computer Wins this round!")
            computer_score += 1

        # Display scores
        print(f"Score: You - {player_score}, Computer - {computer_score}\n")

    # Final results
    print("\nGame Over!")
    print(f"Final Scores: You - {player_score}, Computer - {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif player_score < computer_score:
        print("Better luck next time! The computer won.")
    else:
        print("It's a tie! Well played.")

# Run the game
stone_paper_scissors()
