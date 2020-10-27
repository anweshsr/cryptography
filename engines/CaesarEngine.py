from cipher.cipher import Cipher
from cipher.alphabet import Alphabet


class CaesarCipher(Cipher):
    """
    This engine implements the Caesar Cipher algorithm given a valid key and optional
    args: plaintext alphabet and ciphertext alphabet.
    Example: if key is 3, plaintext 'd' will become 'g' and 'D' will be 'G'
    """

    def __init__(self, spec):
        """
        Creates a CaesarEngine and Alphabet set for the CaesarEngine provided a specification
        for the alphabet. Spec can be in the following patterns:
        SPEC: [key]/[plainalphabet]/[cipheralphabet]
        Key is compulsory. PlainAlphabet and CipherAlphabet are not.
        Key must be an int.
        PlainAlphabet and CipherAlphabet are str.
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
        key, plain_range, cipher_range = spec.split("/")
        self.alphabet = Alphabet(plain_range, cipher_range)
        try:
            self.key = int(key)
        except ValueError:
            raise Exception("Key should be int")
        if len(self.alphabet.plain_alphabet) != len(
                self.alphabet.cipher_alphabet):
            raise Exception("Length of both alphabet arrays not equal")

    def encode_shift(self, ch, key):
        """
        Returns an encoded character for the given character and a given key
        :param ch: str, The character to be encoded
        :param key: key, The key which is needed for encryption
        :return: encoded character
        """
        plain_alphabet = self.alphabet.plain_alphabet
        cipher_alphabet = self.alphabet.cipher_alphabet
        if ord(ch) not in plain_alphabet:
            return ord(ch)
        while key < 0:
            key += len(plain_alphabet)
        return cipher_alphabet[
            (plain_alphabet.index(ord(ch)) + key) % len(plain_alphabet)]

    def decode_shift(self, ch, key):
        """
        Returns a decoded character for the given character and a given key
        :param ch: str, The character to be decoded
        :param key: key, The key which is needed for decryption
        :return: decrypted character
        """
        plain_alphabet = self.alphabet.plain_alphabet
        cipher_alphabet = self.alphabet.cipher_alphabet
        if ord(ch) not in cipher_alphabet:
            return ord(ch)
        while key < 0:
            key += len(cipher_alphabet)
        return plain_alphabet[(cipher_alphabet.index(ord(ch)) +
                               len(cipher_alphabet) - key) % len(cipher_alphabet)]

    def encrypt(self, text):
        """
        Encrypts a whole string
        :param text: str, The string to be encrypted
        :return: Encrypted string
        """
        if not isinstance(text, str):
            return text
        encrypted_str = [chr(self.encode_shift(c, self.key)) for c in text]
        return "".join(encrypted_str)

    def decrypt(self, text):
        """
        Decrypts an encrypted string
        :param text: str, The string to be decrypted
        :return: Decrypted string
        """
        if not isinstance(text, str):
            return text
        decrypted_str = [chr(self.decode_shift(c, self.key)) for c in text]
        return "".join(decrypted_str)
