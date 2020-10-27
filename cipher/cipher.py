from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    Abstract class for Cipher engines.
    """

    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass
