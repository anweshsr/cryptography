from abc import ABC, abstractmethod

class Solver(ABC):
    """
    Abstract class for Cipher Solver
    """

    @abstractmethod
    def setup(self, dictionary):
        pass

    @abstractmethod
    def run(self, text):
        pass