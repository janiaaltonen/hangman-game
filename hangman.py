from random import randrange


class Hangman:

    def __init__(self, filename='hangman_words.txt'):
        self.filename = filename
        self.__words = self.readWords()
        self.used_words = []
        self.__word = {str}
        self.__printable = []
        self.generate()
        self.corrects = set()
        self.missed = set()
        self.guesses = 0

    def readWords(self):
        """
        * method reads guessable words from txt. file and returns them in a tuple
        """
        file = None
        words = []
        try:
            file = open(self.filename, 'r', encoding="utf-8")
            for row in file:
                row = row.strip()
                if len(row) > 0:
                    words.append(row)
            file.close()
        except (FileNotFoundError, IOError) as error:
            print(f'Tiedostoa {self.filename} ei voitu lukea: {error}')
        finally:
            if file is not None:
                file.close()
        return tuple(words)

    def generate(self):
        """
        * method takes random word out of (self.__words)
        * used words are placed in used_words[] so they won't pop up again
        """

        while True:
            word = self.__words[randrange(len(self.__words))]
            if word not in self.used_words:
                self.used_words.append(word)
                self.__word = word
                self.__printable = ['_'] * len(word)
                self.corrects = set()
                self.missed = set()
                self.guesses = 0
                break

    def check(self, letter):
        """
        * method checks if the input_letter is in random word, updates corrects set() and returns True
        * if not in random word updates missed set() and returns False
        * updates guesses (right ones)
        * places input_letter to correct position(s) in printable[]
        """
        index_places = [i for i, e in enumerate(self.__word) if e == letter]
        if len(index_places) > 0:
            self.corrects.add(letter)
            for i in index_places:
                self.__printable[i] = letter.upper()
                self.guesses += 1
            return True
        else:
            self.missed.add(letter)
            return False

    def isWin(self):
        """
        * method checks if game is won
        * if game is won corrects and missed sets() and guesses are reset
        * returns tuple()
        """
        is_won = self.guesses == len(self.__word)
        return is_won

    def reset(self):
        self.generate()
        self.corrects = set()
        self.missed = set()
        self.guesses = 0

    @property
    def getLetters(self):
        return " ".join([str(i) for i in self.__printable])

    @property
    def getWord(self):
        return self.__word
