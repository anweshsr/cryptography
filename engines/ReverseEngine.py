from cipher.cipher import Cipher
from typing import Union

class ReverseCipher(Cipher):
    """
    This engine implements the Reverse Cipher algorithm.
    The algorithm reverses a sequence of characters or bytes.
    Example: if plaintext is 'ab' the ciphertext is 'ba'
    """

    def _reverse(self, text: Union[bytes, bytearray]):
        """
        Reverses bytes
        :param text: str or bytes, string or bytes to be reversed
        :return: reversed str or reversed bytes
        """
        return text[::-1]

    def encrypt(self, text: Union[bytes, bytearray]):
        """
        Encrypts a whole string
        :param text: str, The string to be encrypted
        :return: Encrypted string
        """
        return self._reverse(text)

    def decrypt(self, text: Union[bytes, bytearray]):
        """
        Decrypts bytes
        :param text: str, The string to be decrypted
        :return: Decrypted string
        """
        return self._reverse(text)
