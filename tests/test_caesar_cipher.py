import unittest, csv
import pytest
from engines.CaesarEngine import CaesarCipher

class CaesarCipherTestCase(unittest.TestCase):

    def test_caesar_cipher_key1(self):
        assert CaesarCipher.from_specification("3/az").encrypt("abcd", return_type=str)=="defg"

    def test_caesar_cipher_key3(self):
        assert CaesarCipher.from_specification("27/az").encrypt("abc", return_type=str)=="|}~"

    def test_caesar_cipher_alphabet1(self):
        assert CaesarCipher.from_specification("4/azAZ09").encrypt("aA1")==b"eE5"

    def test_caesar_cipher_alphabet3(self):
        assert CaesarCipher.from_specification("2/all").encrypt("None9👍")==bytearray(b'Pqpg;\xf2\xa1\x93\x8f')

    def test_caesar_cipher_1(self):
        cs = CaesarCipher.from_specification("5/AZaz09")
        assert cs.decrypt(cs.encrypt('abc'), return_type=str) == 'abc'

    def test_caesar_cipher_2(self):
        cs = CaesarCipher.from_specification("31/AZaz09")
        assert cs.decrypt(cs.encrypt('abc'), return_type=str) == 'abc'

    def test_caesar_cipher_3(self):
        cs = CaesarCipher.from_specification("10/AZaz")
        assert cs.decrypt(cs.encrypt('None9👍'), return_type=str) == 'None9👍'

    def test_caesar_cipher_4(self):
        cs = CaesarCipher.from_specification("1/AZaz")
        assert cs.decrypt(cs.encrypt('None9👍'), return_type=str) == 'None9👍'

    def test_caesar_cipher_5(self):
        cs = CaesarCipher.from_specification("1/all")
        assert cs.decrypt(cs.encrypt('ABC')) != 'A'

    def test_caesar_cipher_6(self):
        cs = CaesarCipher.from_specification("27/all")
        assert cs.decrypt(cs.encrypt('ABC')) != 'ACB'

    def test_caesar_encrypt_decrypt_file1(self):
        test_data_file_path = "./test_cases_caesar_cipher_aray.csv"
        test_data_file_object = open(test_data_file_path, 'r', encoding='utf-8')
        csv_reader = csv.reader(test_data_file_object, delimiter=',')
        for row in csv_reader:
            if len(row) == 3:
                cc = CaesarCipher.from_specification(str(row[0]) + "/all")
                assert cc.encrypt(row[1], return_type=str) == row[2]
                assert cc.decrypt(cc.encrypt(row[1]), return_type=str) == row[1]
            elif len(row) == 2:
                cc = CaesarCipher.from_specification(str(row[0]) + "/all")
                assert cc.decrypt(cc.encrypt(row[1]), return_type=str) == row[1]

if __name__ == '__main__':
    unittest.main()
