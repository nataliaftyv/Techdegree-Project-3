import random
from phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [
            'The Remains of the Day',
            'A Pale View of Hills',
            'An Artist of the Floating World ',
            'Never Let Me Go',
            'The Buried Giant'
        ]
        self.active_phrase = None
        self.guesses = []
        # a list that contains the letters guessed by the user.



    def start(self):
        # Calls the welcome method
        self.welcome()
    # creates the game loop,
    # calls the get_guess method, adds the user's guess to guesses
        self.get_guess()
    # increments the number of missed by one if the guess is incorrect,
    # calls the game_over method.
        self.game_over()


    def get_random_phrase(self):
        return random.choice(self.phrases)

    @staticmethod
    def welcome():
        print('Welcome to the Phrase Hunt Game! Can you guess the hidden phrase?')

    def get_guess(self):
        # gets the guess from a user and records it in the guesses attribute
        guess = input('What is your letter guess? > ')
        guess = guess.lower()
        self.guesses.append(guess)


    def game_over(self):
        # this method displays a friendly win or loss message and ends the game.
        if Phrase.check_complete():
            print('You won!')
        elif self.missed > 5:
            print('You lost!')



