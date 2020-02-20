import random


class Game:
    def __init__(self):
        self.start_game()
        self.difficulty = 0
        self.player = Player()
        self.word = self.choose_word()

    def __str__(self):
        return "Hangman style game"

    def get_words(self):
        with open('words.txt', 'r') as f:
            words = f.readlines()
        words = [word.strip().upper() for word in words]
        return words

    def choose_word(self):
        words = self.get_words()
        return random.choice(words)

    def print_progress(self):
        guesses = self.player.guesses
        hit_list = [char if char in guesses else '_' for char in self.word]
        print(' '.join(hit_list))

    def start_game(self):
        pass

    def end_game(self):
        pass


class Bot:
    def __init__(self):
        pass

    def __str__(self):
        return "Evil non-sentient opponent. Or is it?"


class Player:
    def __init__(self):
        self.guesses = []

    def __str__(self):
        return "Courageous human word guesser"

    def guess(self):
        valid = False
        while not valid:
            guess = input("\nGuess a letter: ").upper()
            if not guess.isalpha() or len(guess) != 1:
                print("Enter a single letter.")
                continue
            elif guess in self.guesses:
                print("You've already guessed that letter. Try another.")
                continue
            else:
                valid = True
                self.guesses.append(guess)
        return guess


if __name__ == "__main__":
    pass
