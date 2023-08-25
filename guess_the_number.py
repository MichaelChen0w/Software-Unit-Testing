"""Guess the number"""
import random


class GuessTheNumberGame:
    """Class reprenting Guess The Number Game"""
    def __init__(self):
        self.secret_number = self.generate_random_number()

    def generate_random_number(self):
        """Function: generate random number"""
        return ''.join(random.sample('0123456789', 4))

    def check_guess(self, guess):
        """Function: check guess"""
        if guess == self.secret_number:
            return "Correct"

        circles = 0
        x_count = 0

        for i in range(4):
            if guess[i] == self.secret_number[i]:
                circles += 1
            elif guess[i] in self.secret_number:
                x_count += 1

        return f"{circles} circles, {x_count} x"


if __name__ == "__main__":
    game = GuessTheNumberGame()
    print("Welcome to Guess the Number!")
    print("Type 'quit' to exit the game.")

    attempts = 0  # pylint: disable = invalid-name
    while True:
        guess_ = input("Enter your 4-digit number guess (or 'quit' to exit): ")
        if guess_.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            break
        if not guess_.isdigit() or len(guess_) != 4:
            print("Invalid input. Please enter a valid 4-digit number.")
            continue

        result = game.check_guess(guess_)
        print(result)
        attempts += 1
        if result == "Correct":
            print(f"Congratulations! You guessed number {attempts} attempts")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                game = GuessTheNumberGame()
                attempts = 0  # pylint: disable = invalid-name
            else:
                break
