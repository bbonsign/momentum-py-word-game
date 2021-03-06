import random
from time import sleep


class Game:
    def __init__(self):
        self.word = "CHOCOLATE"
        self.wlen = 9
        self.difficulty = {'min': 0, 'max': 1000}
        # The above will change when game starts
        self.guess_limit = 8
        self.remaining = 8
        self.player = Player()
        self.playing = True

    def __str__(self):
        return "Hangman style game"

    def cmp_word(self):
        return self.word

    def get_words(self):
        with open('words.txt', 'r') as f:
            words = f.readlines()
        words = [word.strip().upper() for word in words]
        return words

    def choose_word(self):
        words = self.get_words()
        word = random.choice(words)
        min, max = self.difficulty['min'], self.difficulty['max']
        while not (min <= len(word) <= max):
            word = random.choice(words)
        self.word = word
        self.wlen = len(word)

    def set_difficulty(self):
        diff_levels = {
            'easy': {'min': 4, 'max': 6},
            'normal': {'min': 6, 'max': 8},
            'hard': {'min': 8, 'max': 1000}
        }
        print(" - Easy: 4-6 letter words")
        print(" - Normal: 6-8 letter words")
        print(" - Hard: 8+ letter words")
        level = input(" Choose easy, normal, or hard: ").lower().strip()
        while level not in ['easy', 'normal', 'hard']:
            level = input(" Choose easy, normal, or hard: ").lower().strip()
        self.difficulty = diff_levels[level]

    def print_progress(self):
        good_guesses = self.player.guesses['correct']
        hit_list = [char if char in good_guesses else '_' for char in self.word]
        print()
        print(' '.join(hit_list))

    def start_game(self):
        self.set_difficulty()
        self.choose_word()
        print(f"\nThe word contains {self.wlen} letters.  Choose wisely!\n")
        print("_ "*self.wlen)
        self.rounds()

    def rounds(self):
        while self.playing:
            decrement = len(self.player.guesses['incorrect'])
            self.remaining = self.guess_limit - decrement
            print('\n'+'='*60)
            print(
                f"\n*** You have {self.remaining} guesses left ***\n")
            self.player.guess()
            guess = self.player.current_guess
            self.word = self.cmp_word()
            if guess in self.word:
                print('   Nice!')
                self.player.guesses['correct'].append(guess)
            else:
                print('   Nope!')
                self.player.guesses['incorrect'].append(guess)
            self.print_progress()
            good_guesses = self.player.guesses['correct']
            join_guesses = ''.join([c for c in self.word if c in good_guesses])
            if join_guesses == self.word:
                self.player.winner = True
                self.playing = False
            elif len(self.player.guesses['incorrect']) == self.guess_limit:
                self.playing = False
                print(
                    f"\n{'='*65}\n{'='*65}\n\n*** *** *** *** You are out of guesses. *** *** *** ***\n")
        self.end_game()

    @staticmethod
    def new_game_prompt():
        newgame = input("\n\nPlay again? (y) or (n): ")
        while not(newgame == 'y' or newgame == 'n'):
            newgame = input("Play again? (y) or (n): ")
        if newgame == 'n':
            exit()
        elif newgame == 'y':
            print('\n\n\n')
            Game().start_game()

    def end_game(self):
        if self.player.winner:
            print("\n You win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print(" *** You lost in a spectacular fashion. ***")
            print(f" *** The correct word was: {self.word} ***")
        sleep(1)
        self.new_game_prompt()


class Player:
    def __init__(self):
        self.guesses = {'correct': [], 'incorrect': []}
        self.winner = False
        self.current_guess = ''

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
        self.current_guess = guess
        # return guess


if __name__ == "__main__":
    Game().start_game()
