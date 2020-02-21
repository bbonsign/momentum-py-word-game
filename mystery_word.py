import random
from time import sleep


class Game:
    def __init__(self):
        # self.word = self.choose_word()
        self.word = "CHOCOLATE"
        self.difficulty = 0
        self.guess_limit = 3
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
        # guesses = self.player.guesses
        good_guesses = self.player.guesses['correct']
        hit_list = [char if char in good_guesses else '_' for char in self.word]
        print()
        print(' '.join(hit_list))

    def start_game(self):
        self.set_difficulty()
        print(
            f"The word contains {len(self.word)} letters.  Good luck chump!\n")
        print("_ "*len(self.word))
        self.rounds()

    def rounds(self):
        while self.playing:
            decrement = len(self.player.guesses['incorrect'])
            print('\n'+'='*60)
            print(
                f"\n*** You have {self.guess_limit-decrement} guesses left ***\n")
            guess = self.player.guess()
            if guess in self.word:
                print('   Nice!')
                self.player.guesses['correct'].append(guess)
            else:
                print('   Nope!')
                self.player.guesses['incorrect'].append(guess)
            self.print_progress()
            good_guesses = self.player.guesses['correct']
            combined_guesses = ''.join([char for char in self.word if char in good_guesses])
            if combined_guesses == self.word:
                self.player.winner = True
                self.playing = False
            elif len(self.player.guesses['incorrect']) == self.guess_limit:
                self.playing = False
                print(f"\n{'='*65}\n{'='*65}\n\n*** *** *** *** You are out of guesses. *** *** *** ***\n")
        # guessed_word = self.player.guess_word()
        # if guessed_word == self.word:
        #     self.player.winner = True
        #     self.playing = False
        self.end_game()

    def end_game(self):
        if self.player.winner:
            print("\n You win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print(" *** You lost in a spectacular fashion. ***")
            print(f" *** The correct word was: {self.word} ***")
        sleep(1)
        newgame = input("Play again? (y) or (n): ")
        while not(newgame == 'y' or newgame == 'n'):
            newgame = input("Play again? (y) or (n): ")
        if newgame == 'n':
            exit()
        elif newgame == 'y':
            Game()


class Player:
    def __init__(self):
        self.guesses = {'correct': [], 'incorrect': []}
        # self.word_guesses = []
        self.winner = False

    def __str__(self):
        return "Courageous human word guesser"

    def all_guesses(self):
        return self.guesses['correct'] + self.guesses['incorrect']

    def guess(self):
        valid = False
        while not valid:
            guess = input(" Guess a letter: ").upper()
            if not guess.isalpha() or len(guess) != 1:
                print("Enter a single letter.")
                continue
            elif guess in self.all_guesses():
                print("You've already guessed that letter. Try another.")
                continue
            else:
                valid = True
        return guess

    # def guess_word(self):
    #     guess = input("\n Guess the word: ").upper()
    #     while not guess.isalpha():
    #         guess = input("\n Guess the word: ").upper()
    #     return guess


if __name__ == "__main__":
    Game()
