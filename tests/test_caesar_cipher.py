import unittest
import pytest
from engines.CaesarEngine import CaesarCipher

class CaesarCipherTestCase(unittest.TestCase):

    def test_caesar_cipher_key1(self):
        assert CaesarCipher.from_specification("3/az").encrypt("abcd")=="defg"

    def test_caesar_cipher_key3(self):
        assert CaesarCipher.from_specification("27/az").encrypt("abc")=="bcd"

    def test_caesar_cipher_alphabet1(self):
        assert CaesarCipher.from_specification("4/azAZ09").encrypt("aA1")=="eE5"

    def test_caesar_cipher_alphabet3(self):
        assert CaesarCipher.from_specification("2/all").encrypt("None9👍")=="Pqpg;👏"

    def test_caesar_cipher_1(self):
        cs = CaesarCipher.from_specification("5/AZaz09")
        assert cs.decrypt(cs.encrypt('abc')) == 'abc'

    def test_caesar_cipher_2(self):
        cs = CaesarCipher.from_specification("31/AZaz09")
        assert cs.decrypt(cs.encrypt('abc')) == 'abc'

    def test_caesar_cipher_3(self):
        cs = CaesarCipher.from_specification("10/AZaz")
        assert cs.decrypt(cs.encrypt('None9👍')) == 'None9👍'

    def test_caesar_cipher_4(self):
        cs = CaesarCipher.from_specification("1/AZaz")
        assert cs.decrypt(cs.encrypt('None9👍')) == 'None9👍'

    def test_caesar_cipher_5(self):
        cs = CaesarCipher.from_specification("1/all")
        assert cs.decrypt(cs.encrypt('ABC')) != 'A'

    def test_caesar_cipher_6(self):
        cs = CaesarCipher.from_specification("27/all")
        assert cs.decrypt(cs.encrypt('ABC')) != 'ACB'

if __name__ == '__main__':
    unittest.main()
