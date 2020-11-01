import sys
from cipher import constants
from functools import partial


def get_range(start, end):
    return range(start, end)


def custom_range(range_options):
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


class AlphabetFactory:
    range_alphabet_map = {
        'all': partial(get_range, 0, sys.maxunicode),
        'ascii': partial(get_range, constants.ASCII_START, constants.ASCII_END),
        'ascii_lowercase': partial(get_range, constants.ASCII_LOWERCASE_START, constants.ASCII_LOWERCASE_END),
        'ascii_uppercase': partial(get_range, constants.ASCII_UPPERCASE_START, constants.ASCII_UPPERCASE_END),
    }

    def get_alphabet_generator(self, range_options):
        if range_options in self.range_alphabet_map:
            return self.range_alphabet_map[range_options]
        return partial(custom_range, range_options)