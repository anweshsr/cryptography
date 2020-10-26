import sys

from crypto.cipher import constants

class Alphabet(object):
    def __init__(self, plain_range_options, cipher_range_options):
        self.plain_range_options = plain_range_options
        self.cipher_range_options = cipher_range_options
        self.plain_alphabet = self.get_alphabets(self.plain_range_options)
        self.cipher_alphabet = self.get_alphabets(self.cipher_range_options)

    def get_alphabets(self, range_options):
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


if __name__ == '__main__':
    alpha = Alphabet('AZ', 'AZ')
    print(alpha.plain_alphabet)
    print(alpha.cipher_alphabet)