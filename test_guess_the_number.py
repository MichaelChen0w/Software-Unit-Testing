"""Test guess number"""
import unittest
from guess_the_number import GuessTheNumberGame


class TestGuessTheNumberGame(unittest.TestCase):
    """Class reprenting Test Guess The Number Game"""
    def test_generate_random_number(self):
        """Function: test generate random number"""
        game = GuessTheNumberGame()
        random_number = game.generate_random_number()
        self.assertIsInstance(random_number, str)
        self.assertEqual(len(random_number), 4)
        self.assertTrue(random_number.isdigit())

    def test_check_guess_with_correct_number(self):
        """Function: test check guess with correct number"""
        game = GuessTheNumberGame()
        game.secret_number = "1234"
        result = game.check_guess("1234")
        self.assertEqual(result, "Correct")

    def test_check_guess_with_incorrect_number(self):
        """Function: test check guess with incorrect number"""
        game = GuessTheNumberGame()
        game.secret_number = "1234"
        result = game.check_guess("5678")
        self.assertEqual(result, "0 circles, 0 x")
        result = game.check_guess("1243")
        self.assertEqual(result, "2 circles, 2 x")
        result = game.check_guess("4321")
        self.assertEqual(result, "0 circles, 4 x")


if __name__ == '__main__':
    unittest.main()
