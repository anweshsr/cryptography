import unittest
import pytest
from engines.ReverseEngine import ReverseCipher

class ReverseCipherTestCase(unittest.TestCase):

    def test_reverse_cipher1(self):
        assert ReverseCipher().encrypt('abcd') == 'dcba'

    def test_reverse_cipher2(self):
        assert ReverseCipher().encrypt(b'abc') == b'cba'

    def test_reverse_cipher3(self):
        assert ReverseCipher().encrypt(bytes('None9👍'.encode()))==b'\x8d\x91\x9f\xf09enoN'

    def test_reverse_cipher4(self):
        assert ReverseCipher().encrypt(None) == None

    def test_reverse_cipher5(self):
        assert ReverseCipher().encrypt(12345) == 12345

    def test_reverse_cipher6(self):
        assert ReverseCipher().encrypt('abcd') != 'dcb'

if __name__ == '__main__':
    unittest.main()
