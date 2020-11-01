from cipher.cipher import Cipher


class ReverseCipher(Cipher):
    """
    This engine implements the Reverse Cipher algorithm.
    The algorithm reverses a sequence of characters or bytes.
    Example: if plaintext is 'ab' the ciphertext is 'ba'
    """

    def _reverse(self, text):
        """
        Reverses a str or bytes
        :param text: str or bytes, string or bytes to be reversed
        :return: reversed str or reversed bytes
        """
        if isinstance(text, (bytes, str)):
            return text[::-1]
        return text

    def encrypt(self, text):
        """
        Encrypts a whole string
        :param text: str, The string to be encrypted
        :return: Encrypted string
        """
        return self._reverse(text)

    def decrypt(self, text):
        """
        Decrypts an encrypted string
        :param text: str, The string to be decrypted
        :return: Decrypted string
        """
        return self._reverse(text)
