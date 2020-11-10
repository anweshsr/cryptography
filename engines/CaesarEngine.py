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
        assert type(key) == int
        self.key = key
        self.alphabet = alphabet

    @classmethod
    def from_specification(cls, spec):
        key, range_options = spec.split("/")
        key = int(key)
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

    def encrypt_bytes(self, byte_array, key):
        byte_length = self.alphabet.byte_length
        for i in range(len(byte_array)):
            byte_array[i] = (byte_array[i] + key) % byte_length
        return byte_array

    def encrypt(self, text, return_type=None):
        """
        Encrypts a whole string
        :param text: str, The string to be encrypted
        :return: Encrypted string
        """
        if not isinstance(text, (str, bytearray, bytes)):
            return text
        alphabet = self.alphabet.alphabet
        key = self.key
        while key < 0:
            key += len(alphabet)
        bstring = bytearray(text, self.alphabet.encoding) if type(text) == str else bytearray(text)
        bstring = self.encrypt_bytes(bstring, key)
        if return_type == str:
            bstring = bstring.decode(self.alphabet.encoding)
        return bstring

    def decrypt_bytes(self, byte_array, key):
        byte_length = self.alphabet.byte_length
        for i in range(len(byte_array)):
            byte_array[i] = (byte_array[i] - key) % byte_length
        return byte_array

    def decrypt(self, text, return_type=None):
        """
        Decrypts an encrypted string
        :param text: str, The string to be decrypted
        :return: Decrypted string
        """
        if not isinstance(text, (str, bytearray)):
            return text
        alphabet = self.alphabet.alphabet
        key = self.key
        while key < 0:
            key += len(alphabet)
        bstring = bytearray(text, self.alphabet.encoding) if isinstance(text, str) else text
        bstring = self.decrypt_bytes(bstring, key)
        if return_type == str:
            bstring = bstring.decode(self.alphabet.encoding)
        return bstring

if __name__ == '__main__':
    cc =  CaesarCipher.from_specification("1/all")
    print(cc.encrypt("^%$", return_type=str))
    print(cc.decrypt(cc.encrypt("abc"), return_type=str))

