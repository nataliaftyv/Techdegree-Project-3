import copy
from game import Game


class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_as_list = list(self.phrase)

    def display(self):
        # display phrase, un-guessed letters as dash, guessed as letter
        # TODO: try to not have loop every time, hold display phrase, replace if check_letter is true
        guessed_letters = self.check_letter()
        display_phrase_list = copy.deepcopy(self.phrase_as_list)
        for letter in guessed_letters:
            for i in range(len(display_phrase_list)):
                if display_phrase_list[i] is letter:
                    display_phrase_list[i] = letter
                elif display_phrase_list[i] is not ' ':
                    display_phrase_list[i] = '-'

        display_phrase = ''.join(display_phrase_list)
        return display_phrase

    def check_letter(self):
        # checks to see if the letter selected by the user matches a letter in the phrase.
        # hidden_phrase_list = copy.deepcopy(self.phrase_as_list)
        # TODO: try by returning the letter if true
        guessed_letters = []
        letter = Game.get_guess
        if letter in self.phrase_as_list:
            guessed_letters.append(letter)
        return guessed_letters

    def check_complete(self, display_phrase):
        if '-' not in display_phrase:
            return True
        # checks to see if the whole phrase has been guessed
        # TODO: figure this out, should  not be static


