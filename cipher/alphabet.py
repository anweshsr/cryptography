import sys

from cipher import constants


class Alphabet(object):
    """
    This class sets the alphabet based on the alphabet_range_options provided
    Generally both of them are identical. Encryption encodes a character
    """

    def __init__(self, alphabet_range_options):
        """
        Initializes Alphabet, sets the alphabet based on the alphabet range provided
        based on the range options provided.
        :param plain_range_options: str, Range options for plaintext alphabet
        :param cipher_range_options: str, Range options for ciphertext alphabet
        """
        self.alphabet_range_options = alphabet_range_options
        self.alphabet = self.get_alphabets(self.alphabet_range_options)

    def get_alphabets(self, range_options):
        """
        ##TODO: Implement factory pattern to get alphabet
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
        if range_options == 'all':
            return range(sys.maxunicode)
        if range_options == 'ascii':
            return range(constants.ASCII_START, constants.ASCII_END)
        if range_options == 'ascii_lowercase':
            return range(constants.ASCII_LOWERCASE_START, constants.ASCII_LOWERCASE_END)
        if range_options == 'ascii_uppercase':
            return range(constants.ASCII_UPPERCASE_START, constants.ASCII_UPPERCASE_END)
        range_options = list(range_options)
        start_chars = range_options[0::2]
        end_chars = range_options[1::2]
        if len(start_chars) != len(end_chars):
            raise Exception("Range not properly provided")
        chars_list = []
        for tup in zip(start_chars, end_chars):
            start = tup[0]
            end = tup[1]
            chars_list += [c for c in range(ord(start), ord(end) + 1)]
        return sorted(chars_list)
