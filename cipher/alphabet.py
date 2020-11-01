from cipher.alphabet_factory import AlphabetFactory


class Alphabet(object):
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

    def get_alphabets(self, range_options):
        """
        Generates the alphabet set given range_options.
        Following are the types of alphabet ranges:
            1. all              : All unicode characters are part of alphabet
            2. ascii            : Only ascii characters are part of alphabet
            3. ascii_lowercase  : Only ascii lowercase characters are part of alphabet
            4. ascii_uppercase  : Only ascii uppercase characters are part of alphabet
            5. customrange      : This needs to be series of pairs such as p1p2p3 where each pair
                                  is a tuple of start and end chars of that pair.
                                  Like azAZ09 means all chars in set{a..z, A..Z, 0..9}
        :param range_options: str, ranges provided like above
        :return: alphabet set for given range
        """
        alphabet_factory = AlphabetFactory()
        alphabet_generator = alphabet_factory.get_alphabet_generator(range_options)
        alphabet = alphabet_generator()
        return alphabet