from solver.solverr import Solver
from engines.CaesarEngine import CaesarCipher
from util.trie import Dictionary


class CaesarSolver(Solver):
    """
    This solver does a brute-force approach where it takes all possible keys and decrypts the text.
    The words of the text are checked in a dictionary. We take the best decryption as the one with
    the highest number of matches
    """
    def setup(self, dictionary):
        """
        Sets up the solver. Sets a dictionary to the solver
        :param dictionary:
        :return:
        """
        self.dictionary = dictionary

    def analyze(self, text, dictionary, key_range, alphabet):
        """
        This method gives the best caesar engine which solves the encrypted text. It returns None if
        there is no match in the given dictionary.
        :param text: str, encrypted text
        :param dictionary: Dictionary, dictionary containing all words
        :param key_range: int, maximum value of key to be evaluated
        :param alphabet: Alphabet, alphabet set of the text
        :return: CaesarEngine
        """
        max_stats = 0
        best_engine = None
        for key in range(key_range):
            engine = CaesarCipher(key, alphabet)
            words = text.split(engine.encrypt(" "))
            stats = self.get_stats(words, engine, dictionary)
            if stats > max_stats:
                max_stats = stats
                best_text = ""
                for word in words:
                    best_text += (engine.decrypt(word) + " ")
                best_engine = engine
        return best_engine if best_engine!=None else None

    def search(self, text, dictionary):
        """
        Searches the text in the dictionary. Return 1 if found else 0
        :param text: str, decrypted text
        :param dictionary: Dictionary, dictionary with words
        :return: 1/0
        """
        return 1 if text.lower() in dictionary else 0

    def get_stats(self, text, cipher, dictionary):
        """
        Currently returns total number of matches a decrypted text has in a dictionary.
        TODO: Improve this to give score and also generate a proper report
        :param text: str, encrypted text
        :param cipher: CaesarEngine, Cipher required to decrypt
        :param dictionary: Dictionary, dictionary containing the words
        :return: int, total words matching in dictionary after decryption
        """
        total_matches = 0
        for word in text:
            raw_text = cipher.decrypt(word)
            match = self.search(raw_text, dictionary)
            total_matches += match
        return total_matches

    def run(self, text, alphabet):
        """
        Sets the key_range. Currently set to 255.
        Analyses the text by decrypting and checking in dictionary for all possible keys.
        Prints the best match
        TODO: Work on key_range
        :param text:
        :param alphabet:
        :return:
        """
        key_range = 255
        engine = self.analyze(text, self.dictionary, key_range, alphabet)
        print(engine.decrypt(text))


if __name__ == '__main__':
    #TODO: Remove after writing test cases
    solver = CaesarSolver()
    dictionary = Dictionary.from_txt("english-20k-words.txt")
    cipher = CaesarCipher.from_specification("1/all")
    print(cipher.encrypt("Abtin Rahimian Anwesh Sinha Ray"))
    solver.setup(dictionary)
    from cipher import alphabet
    solver.run("Bcujo!Sbijnjbo!Boxfti!Tjoib!Sbz", alphabet.Alphabet("all"))