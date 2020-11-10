from cipher.alphabet_factory import AlphabetFactory


class Alphabet:
    """
    This class sets the alphabet based on the alphabet_range_options provided
    Generally both of them are identical. Encryption encodes a character
    """

    def __init__(self, alphabet_range_options):
        """
        Initializes Alphabet, sets the alphabet based on the alphabet range provided
        based on the range options provided.
        :param alphabet_range_options: str, Range options for alphabet
        """
        self.alphabet_range_options = alphabet_range_options
        self.alphabet = self.get_alphabets(self.alphabet_range_options)
        self.byte_length = 256
        self.encoding = "utf-8"

    def get_alphabets(self, range_options):
        """
        Generates the alphabet set given range_options.
        :param range_options: str, ranges provided like above
        :return: alphabet set for given range
        """
        alphabet_factory = AlphabetFactory()
        alphabet_generator = alphabet_factory.get_alphabet_generator(range_options)
        alphabet = alphabet_generator()
        return alphabet