import random

def play_game(best_score=None):
    print("\n Welcome to the Number Guessing Game!")

    while True:
        try:
            min_val = int(input("Enter the minimum number: "))
            max_val = int(input("Enter the maximum number: "))
            if min_val >= max_val:
                print(" Minimum must be less than maximum. Try again.")
            else:
                break
        except ValueError:
            print(" Please enter valid integers.")


    secret_number = random.randint(min_val, max_val)

    max_attempts = int((max_val - min_val) * 0.3) 
    max_attempts = max(5, min(max_attempts, 15))  
    print(f"\nYou have {max_attempts} attempts to guess the number!")

    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} → Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f" Correct! You guessed it in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(" New best score!")

                print(f"Your best score so far: {best_score} attempts.")
                break
            elif guess < secret_number:
                print("🔼 Too low! Try again.")
            else:
                print("🔽 Too high! Try again.")

        except ValueError:
            print(" Please enter a valid number.")

    else:
        print(f"\n Out of attempts! The correct number was {secret_number}.")

    return best_score


# Main game loop
def main():
    best_score = None
    while True:
        best_score = play_game(best_score)
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("\n Thanks for playing! Final best score:", best_score)
            break

if __name__ == "__main__":
    main()
