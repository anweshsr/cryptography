from cipher.cipher import Cipher
import typing


class CaesarCipher(Cipher):
    """
    This engine implements the Caesar Cipher algorithm given a valid key
    Example: if key is 3, plaintext 'd' will become 'g' and 'D' will be 'G'
    """

    def __init__(self, key: int):
        """
        Creates a CaesarEngine provided a key as positive integer.
        Key must be an int.
        :param key: int
        """
        assert type(key) == int
        assert key > 0
        self.key = key
        self.byte_length = 256

    @classmethod
    def from_specification(cls, key: typing.Union[str,int]):
        key = int(key)
        return cls(key)

    def encrypt(self, barray: bytearray) -> bytearray:
        """
        Encrypts a whole byte array
        :param bytearray: bytearray, The bytes to be encrypted
        :return: Encrypted bytes
        """
        key = self.key
        byte_length = 256
        for i in range(len(barray)):
            barray[i] = (barray[i] + key) % byte_length
        return barray

    def decrypt(self, barray: bytearray) -> bytearray:
        """
        Decrypts an encrypted byte array
        :param bytearray: bytearray, The byte array to be decrypted
        :return: Decrypted bytes
        """
        key = self.key
        byte_length = 256
        for i in range(len(barray)):
            barray[i] = (barray[i] - key) % byte_length
        return barray

