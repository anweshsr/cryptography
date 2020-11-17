from solver.solverr import Solver
from engines.TranspositionEngine import TranspositionCipher

class TranspositionSolver(Solver):

    def setup(self, dictionary):
        self.dictionary = dictionary


    def analyze(self, text, dictionary, key_range):
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
        for key in range(1, key_range):
            engine = TranspositionCipher(key, "$")
            try:
                words = text.split(engine.encrypt(bytearray(" ", "utf-8")).decode("utf-8", errors="ignore"))
            except ValueError:
                continue
            stats = self.get_stats(words, engine, dictionary)
            if stats > max_stats:
                max_stats = stats
                best_text = ""
                for word in words:
                    best_text += (engine.decrypt(bytearray(word,"utf-8")).decode("utf-8") + " ")
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
        :param text: str, encrypted text
        :param cipher: CaesarEngine, Cipher required to decrypt
        :param dictionary: Dictionary, dictionary containing the words
        :return: int, total words matching in dictionary after decryption
        """
        total_matches = 0
        for word in text:
            print(word)
            byte_text = cipher.decrypt(bytearray(word, "utf-8"))
            raw_text = byte_text.decode("utf-8", errors="ignore")
            match = self.search(raw_text, dictionary)
            total_matches += match
        return total_matches

    def run(self, text):
        """
        Sets the key_range. Currently set to 255.
        Analyses the text by decrypting and checking in dictionary for all possible keys.
        Prints the best match
        :param text:
        :param alphabet:
        :return:
        """
        key_range = len(text)
        engine = self.analyze(text, self.dictionary, key_range)
        return engine

if __name__ == '__main__':
    tc = TranspositionCipher.from_specification("2")
    from util.trie import Dictionary
    dictionary = Dictionary.from_txt("english-20k-words.txt")
    print(tc.encrypt(bytearray("a man was here", "utf-8")))
    solver = TranspositionSolver()
    solver.setup(dictionary)
    solver.run('amnwshr a a ee')
    print(tc.decrypt(bytearray('amnwshr a a ee',"utf-8")))