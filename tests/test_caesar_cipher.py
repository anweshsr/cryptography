import unittest, csv
import pytest
from engines.CaesarEngine import CaesarCipher

class CaesarCipherTestCase(unittest.TestCase):

    def test_caesar_cipher_key1(self):
        assert CaesarCipher.from_specification("3").encrypt(bytearray("abcd", "utf-8"))==bytearray("defg", "utf-8")

    def test_caesar_cipher_key3(self):
        assert CaesarCipher.from_specification("27").encrypt(bytearray("abc", "utf-8"))==bytearray("|}~", "utf-8")

    def test_caesar_cipher_alphabet1(self):
        assert CaesarCipher.from_specification("4").encrypt(bytearray("aA1", "utf-8"))==bytearray("eE5", "utf-8")

    def test_caesar_cipher_alphabet3(self):
        assert CaesarCipher.from_specification("2").encrypt(bytearray("None9👍", "utf-8"))==bytearray(b'Pqpg;\xf2\xa1\x93\x8f')

    def test_caesar_cipher_1(self):
        cs = CaesarCipher.from_specification("5")
        assert cs.decrypt(cs.encrypt(bytearray('abc', "utf-8"))) == bytearray('abc', "utf-8")

    def test_caesar_cipher_2(self):
        cs = CaesarCipher.from_specification("31")
        assert cs.decrypt(cs.encrypt(bytearray('abc', "utf-8"))) == bytearray('abc', "utf-8")

    def test_caesar_cipher_3(self):
        cs = CaesarCipher.from_specification("10")
        assert cs.decrypt(cs.encrypt(bytearray('None9👍', "utf-8"))) == bytearray('None9👍', "utf-8")

    def test_caesar_cipher_4(self):
        cs = CaesarCipher.from_specification("1")
        assert cs.decrypt(cs.encrypt(bytearray('None9👍', "utf-8"))) == bytearray('None9👍', "utf-8")

    def test_caesar_cipher_5(self):
        cs = CaesarCipher.from_specification("1")
        assert cs.decrypt(cs.encrypt(bytearray('ABC', "utf-8"))) != bytearray('A', "utf-8")

    def test_caesar_cipher_6(self):
        cs = CaesarCipher.from_specification("27")
        assert cs.decrypt(cs.encrypt(bytearray('ABC', "utf-8"))) != bytearray('ACB', "utf-8")

    def test_caesar_encrypt_decrypt_file1(self):
        test_data_file_path = "./test_cases_caesar_cipher_aray.csv"
        test_data_file_object = open(test_data_file_path, 'r', encoding='utf-8')
        csv_reader = csv.reader(test_data_file_object, delimiter=',')
        for row in csv_reader:
            if len(row) == 3:
                cc = CaesarCipher.from_specification(str(row[0]))
                assert cc.encrypt(bytearray(row[1], "utf-8")) == bytearray(row[2], "utf-8")
                assert cc.decrypt(cc.encrypt(bytearray(row[1], "utf-8"))) == bytearray(row[1], "utf-8")
            elif len(row) == 2:
                cc = CaesarCipher.from_specification(str(row[0]))
                assert cc.decrypt(cc.encrypt(bytearray(row[1], "utf-8"))) == bytearray(row[1], "utf-8")

if __name__ == '__main__':
    unittest.main()
