from cipher.cipher import Cipher
from cipher.alphabet import Alphabet


class CaesarCipher(Cipher):
    """
    This engine implements the Caesar Cipher algorithm given a valid key and optional
    args: alphabet
    Example: if key is 3, plaintext 'd' will become 'g' and 'D' will be 'G'
    """

    def __init__(self, key, alphabet):
        """
        Creates a CaesarEngine and Alphabet set for the CaesarEngine provided a specification
        for the alphabet. Spec can be in the following patterns:
        SPEC: [key]/[alphabet]
        Key is compulsory. Alphabet is not.
        Key must be an int.
        Alphabet is str.
        Following are the types of alphabet ranges:
            1. all              : All unicode characters are part of alphabet
            2. ascii            : Only ascii characters are part of alphabet
            3. ascii_lowercase  : Only ascii lowercase characters are part of alphabet
            4. ascii_uppercase  : Only ascii uppercase characters are part of alphabet
            5. customrange      : This needs to be series of pairs such as p1p2p3 where each pair
                                  is a tuple of start and end chars of that pair.
                                  Like azAZ09 means all chars in set{a..z, A..Z, 0..9}
        :param spec: str, The specifications on which Alphabet is built for the cipher
        """
        try:
            self.key = int(key)
        except ValueError:
            raise Exception("Key should be int")
        self.alphabet = alphabet

    @classmethod
    def from_specification(cls, spec):
        key, range_options = spec.split("/")
        alphabet = Alphabet(range_options)
        return cls(key, alphabet)

    def encode_shift(self, ch, key):
        """
        Returns an encoded character for the given character and a given key
        :param ch: str, The character to be encoded
        :param key: key, The key which is needed for encryption
        :return: encoded character
        """
        alphabet = self.alphabet.alphabet
        if ord(ch) not in alphabet:
            return ord(ch)
        return alphabet[
            (alphabet.index(ord(ch)) + key) % len(alphabet)]

    def decode_shift(self, ch, key):
        """
        Returns a decoded character for the given character and a given key
        :param ch: str, The character to be decoded
        :param key: key, The key which is needed for decryption
        :return: decrypted character
        """
        alphabet = self.alphabet.alphabet
        if ord(ch) not in alphabet:
            return ord(ch)
        return alphabet[(alphabet.index(ord(ch)) +
                         len(alphabet) - key) % len(alphabet)]

    def encrypt(self, text):
        """
        Encrypts a whole string
        :param text: str, The string to be encrypted
        :return: Encrypted string
        """
        if not isinstance(text, str):
            return text
        alphabet = self.alphabet.alphabet
        key = self.key
        while key < 0:
            key += len(alphabet)
        encrypted_str = [chr(self.encode_shift(c, key)) for c in text]
        return "".join(encrypted_str)

    def decrypt(self, text):
        """
        Decrypts an encrypted string
        :param text: str, The string to be decrypted
        :return: Decrypted string
        """
        if not isinstance(text, str):
            return text
        alphabet = self.alphabet.alphabet
        key = self.key
        while key < 0:
            key += len(alphabet)
        decrypted_str = [chr(self.decode_shift(c, self.key)) for c in text]
        return "".join(decrypted_str)
