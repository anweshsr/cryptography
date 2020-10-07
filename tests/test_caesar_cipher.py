import unittest
import pytest
from crypto.engines.CaesarEngine import CaesarCipher

class CaesarCipherTestCase(unittest.TestCase):

    def test_caesar_cipher_key1(self):
        assert CaesarCipher("3/az/az").encrypt("abcd")=="defg"

    def test_caesar_cipher_key2(self):
        with pytest.raises(Exception, match="Key should be int"):
            CaesarCipher("c/az/az")

    def test_caesar_cipher_key3(self):
        assert CaesarCipher("27/az/az").encrypt("abc")=="bcd"

    def test_caesar_cipher_alphabet1(self):
        assert CaesarCipher("4/azAZ09/azAZ09").encrypt("aA1")=="eE5"

    def test_caesar_cipher_alphabet2(self):
        with pytest.raises(Exception, match="Length of both alphabet arrays "
                                            "not equal"):
            CaesarCipher("4/azAZ/az")

    def test_caesar_cipher_alphabet3(self):
        assert CaesarCipher("2/azAZ/azAZ").encrypt("None9👍")=="Pqpg9👍"

    def test_caesar_cipher_1(self):
        cs = CaesarCipher("5/AZaz09/AZaz09")
        assert cs.decrypt(cs.encrypt('abc')) == 'abc'

    def test_caesar_cipher_2(self):
        cs = CaesarCipher("31/AZaz09/AZaz09")
        assert cs.decrypt(cs.encrypt('abc')) == 'abc'

    def test_caesar_cipher_3(self):
        cs = CaesarCipher("10/AZaz/AZaz")
        assert cs.decrypt(cs.encrypt('None9👍')) == 'None9👍'

    def test_caesar_cipher_4(self):
        cs = CaesarCipher("1/AZaz/azAZ")
        assert cs.decrypt(cs.encrypt('None9👍')) == 'None9👍'


if __name__ == '__main__':
    unittest.main()
