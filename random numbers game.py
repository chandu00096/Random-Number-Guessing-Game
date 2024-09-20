import random
import time

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
def select_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Invalid input! Please select a valid difficulty level.")

def play_game():
    # Start by displaying the welcome message and selecting difficulty
    welcome_message()
    chances = select_difficulty()
    
    # Random number generation between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    while chances > 0:
        try:
            guess = int(input(f"\nYou have {chances} chances left. Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess > number_to_guess:
            print("Incorrect! The number is less than your guess.")
        else:
            print("Incorrect! The number is greater than your guess.")
        
        chances -= 1
    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    if chances == 0:
        print(f"\nSorry, you've run out of chances. The number was {number_to_guess}.")
    
    print(f"You took {time_taken} seconds to finish the game.")

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            print("Thank you for playing the Number Guessing Game!")
            return False
        else:
            print("Please enter a valid response (yes or no).")

def main():
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()
