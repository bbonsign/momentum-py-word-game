from mystery_word import Game


class Melkor(Game):
    '''
    Redefine cmp_word to act deceitfully
    '''

    def __init__(self):
        super().__init__()
        self.word_classes = None

    @staticmethod
    def det_class(word, parent, guess):
        class_list = [guess if char == guess
                      else char if char in parent
                      else '-' for char in word]
        return ''.join(class_list)

    def new_word_classes(self):
        guess = self.player.current_guess
        new_classes = {}
        for parent, word_list in self.word_classes.items():
            for word in word_list:
                key = self.det_class(word, parent, guess)
                new_classes.setdefault(key, [])
                new_classes[key].append(word)
        self.word_classes = new_classes

    def cmp_word(self):
        if self.remaining == 8:
            words = [word for word in self.get_words() if len(word) == self.wlen]
            key = ''.join(['-' for i in range(self.wlen)])
            self.word_classes = {key: words}
        self.new_word_classes()
        key, value = max(self.word_classes.items(), key=lambda item: len(item[1]))
        self.word_classes = {key: value}
        if self.remaining == 1:
            self.word = value[0]
            return value[0]
        return key

    @staticmethod
    def new_game_prompt():
        newgame = input("\n\nPlay again? (y) or (n): ")
        while not(newgame == 'y' or newgame == 'n'):
            newgame = input("Play again? (y) or (n): ")
        if newgame == 'n':
            exit()
        elif newgame == 'y':
            print('\n\n\n')
            Melkor().start_game()


if __name__ == "__main__":
    Melkor().start_game()
