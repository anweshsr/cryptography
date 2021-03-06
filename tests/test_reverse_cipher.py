import unittest, csv
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

    def test_caesar_encrypt_decrypt_file1(self):
        test_data_file_path = "./test_cases_reverse_cipher_aray.csv"
        test_data_file_object = open(test_data_file_path, 'r', encoding='utf-8')
        csv_reader = csv.reader(test_data_file_object, delimiter=',')
        for row in csv_reader:
            print(row)
            if len(row) == 2:
                rc = ReverseCipher()
                assert rc.encrypt(row[0]) == row[1]
                assert rc.decrypt(rc.encrypt(row[0])) == row[0]

if __name__ == '__main__':
    unittest.main()
