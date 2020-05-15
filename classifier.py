class Classifier:
    """Class has (at least) one problem:
    when more than object are created from class, duplicate words are written to files.
    e.g. file 'expert.txt' has 2 times same words if 2 objects are created and so on.
    Now no time to fix this bug but in next version will be fixed if needed further.
    """

    def __init__(self):
        self.__words = None
        self.dataPath = "data/"

    def read(self, filename='hangman_words.txt'):
        """
        """
        file = None
        words = []
        try:
            file = open(filename, 'r', encoding="utf-8")
            for row in file:
                row = row.strip()
                if len(row) > 0:
                    words.append(row)
            file.close()
        except (FileNotFoundError, IOError) as error:
            print(f'Tiedostoa hangman_words.txt ei voitu lukea: {error}')
        finally:
            if file is not None:
                file.close()
        self.__words = tuple(words)

    def classify(self):
        """

        """
        frequency_of_letter = {'a': 0.116222, 'i': 0.107077, 't': 0.098779, 'n': 0.086701, 'e': 0.082103, 's': 0.078612,
                               'l': 0.05759, 'o': 0.053091, 'k': 0.052735, 'u': 0.04998, 'ä': 0.048063, 'm': 0.035061,
                               'v': 0.024476, 'r': 0.02163, 'j': 0.019303, 'h': 0.018229, 'y': 0.018123, 'p': 0.016609,
                               'd': 0.008424, 'ö': 0.004741, 'g': 0.001055, 'b': 0.000526, 'f': 0.000491, 'c': 0.000277,
                               'w': 8.36E-05, 'å': 1.32E-05, 'q': 6.61E-06, 'x': 0, 'z': 0, '-': 0}
        raw_difficulty = 0
        avg_len_of_word = 7.46
        expert_level = 0.00035
        demonstration_level = 11.695
        ratio = demonstration_level / expert_level / 4
        for word in self.__words:
            length_of_word = len(word)
            for letter in word:
                # if word contains letter z or x then use q's frequency otherwise there'll be error
                if frequency_of_letter[letter] == 0:
                    raw_difficulty += 1 / length_of_word * (1 / frequency_of_letter['q'])
                # if word's frequency is below letter r's frequency
                # then use frequency and not frequency's multiplicative inverse
                elif frequency_of_letter[letter] < 0.02163:
                    raw_difficulty += 1 / length_of_word * frequency_of_letter[letter]
                else:
                    raw_difficulty += 1 / length_of_word * (1 / frequency_of_letter[letter])
            # added more weight to word's length because its harder to guess randomly longer word
            raw_difficulty = raw_difficulty / (length_of_word * 2 / avg_len_of_word)
            if raw_difficulty >= demonstration_level:
                self.save('demonstration', word)
            elif demonstration_level > raw_difficulty >= expert_level * ratio * 3:
                self.save('easy', word)
            elif expert_level * ratio * 3 > raw_difficulty >= expert_level * ratio * 2:
                self.save('intermediate', word)
            elif expert_level * ratio * 2 > raw_difficulty >= expert_level * ratio * 1:
                self.save('difficult', word)
            else:
                self.save('expert', word)
            raw_difficulty = 0

    def save(self, difficulty, word):
        levels = {'demonstration': 'demonstration', 'easy': 'easy', 'intermediate': 'intermediate',
                  'difficult': 'difficult', 'expert': 'expert'}
        filename = levels[difficulty] + '.txt'
        file = None
        try:
            file = open(self.dataPath + filename, 'a', encoding="utf-8")
            file.write(word + '\n')
            file.close()
        except IOError as e:
            print(f'Tiedostoon {filename} ei voitu kirjoittaa: {e}')
        finally:
            if file is not None:
                file.close()

    def readWords(self, difficulty=0):
        levels = {0: 'demonstration', 1: 'easy', 2: 'intermediate',
                  3: 'difficult', 4: 'expert'}
        filename = levels[difficulty] + '.txt'
        file = None
        words = []
        try:
            file = open(self.dataPath + filename, 'r', encoding="utf-8")
            for row in file:
                row = row.strip()
                if len(row) > 0:
                    words.append(row)
            file.close()
        except (FileNotFoundError, IOError) as e:
            print(f'Tiedostoa {filename} ei voitu lukea: {e}')
        finally:
            if file is not None:
                file.close()
        return tuple(words)
