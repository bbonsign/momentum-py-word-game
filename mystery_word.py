import random


class Game:
    def __init__(self):
        self.word = self.choose_word()
        self.difficulty = 0
        self.player = Player()
        self.playing = True
        self.start_game()

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

    def set_difficulty(self):
        pass

    def print_progress(self):
        guesses = self.player.guesses
        hit_list = [char if char in guesses else '_' for char in self.word]
        print(' '.join(hit_list))

    def start_game(self):
        self.set_difficulty()
        print(f"The word contains {len(self.word)} letters.  Good luck chump!")
        self.rounds()

    def rounds(self):
        while self.playing:
            self.player.guess()
            self.print_progress()
            guesses = self.player.guesses
            combined_guesses = ''.join([char for char in self.word if char in guesses])
            if combined_guesses == self.word:
                self.player.winner = True
                self.playing = False
            elif len(self.player.guesses == 8):
                self.playing = False
        self.end_game()

    def end_game(self):
        if self.player.winner:
            print("You win!!!")
        else:
            print("You lost in a spectacular fashion.")



class Player:
    def __init__(self):
        self.guesses = []
        self.winner = False

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
    Game()