class Game:
    """A game of snowman"""

    def __init__(self, word, tries=5):
        """start a game and define the secret word"""
        self.word = word
        self.word_list = list(word)
        self.tries = tries
        self.wrong_guesses = 0
        self.right_guesses = 0
        self.guesses = []
        self.revealed_letters = []
        self.word_revealed = False
        self.allowed_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                "r",
                                "s", "t", "u", "v", "w", "x", "y", "z"]
        for letter in self.word_list:
            self.revealed_letters.append("_")
        # A beautiful melting snowman
        self.ascii_art = []
        self.ascii_art.append('     _|@|_\n      (")\n  >--( : )--<\n    (  :  )')
        self.ascii_art.append('          \n      (")\n  >--( : )--<\n    (  :  )')
        self.ascii_art.append('          \n      (")\n     ( : )--<\n    (  :  )')
        self.ascii_art.append('          \n      (")\n     ( : )   \n    (  :  )')
        self.ascii_art.append('          \n         \n     ( : )   \n    (  :  )')
        self.ascii_art.append('          \n         \n             \n    (  :  )')
        self.ascii_art.append('          \n         \n             \n           ')

    def repeat_letter(self, guess):
        if guess in self.guesses:
            return True
        else:
            return False

    def guess(self, guess):
        self.guesses.append(guess)
        if guess in self.word_list:
            x = 0
            for letter in self.word_list:
                if guess == self.word_list[x]:
                    self.revealed_letters[x] = guess
                x += 1
            if "_" not in self.revealed_letters:
                self.word_revealed = True
            self.right_guesses += 1
            return True
        else:
            self.wrong_guesses += 1
            return False

    def guesses(self):
        return sorted(self.guesses)

    def revealed_word(self):
        word_so_far = ""
        for letter in self.revealed_letters:
            word_so_far += f" {letter}"
        return word_so_far

    def valid_guess(self, guess):
        return len(guess) == 1 and guess in self.allowed_letters

    def get_snowman(self):
        return self.ascii_art[self.wrong_guesses]
