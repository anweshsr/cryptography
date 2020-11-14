import unittest
from engines.TranspositionEngine import TranspositionCipher

class TranspositionCipherTestCase(unittest.TestCase):
    def test_transposition_cipher1(self):
        tc = TranspositionCipher.from_specification("5/$")
        assert tc.decrypt(tc.encrypt("1234567"), return_type=str) == "1234567"


if __name__ == '__main__':
    unittest.main()
