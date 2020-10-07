from abc import ABC, abstractmethod

class Cipher(ABC):

    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass
