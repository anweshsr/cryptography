import unittest, csv
from engines.TranspositionEngine import TranspositionCipher


class TranspositionCipherTestCase(unittest.TestCase):
    def test_transposition_cipher1(self):
        tc = TranspositionCipher.from_specification("5/$")
        assert tc.decrypt(tc.encrypt(b"1234567")) == b"1234567"

    def test_caesar_encrypt_decrypt_file1(self):
        test_data_file_path = "./test_cases_transposition_cipher_aray.csv"
        test_data_file_object = open(test_data_file_path, 'r', encoding='utf-8')
        csv_reader = csv.reader(test_data_file_object, delimiter=',')
        for row in csv_reader:
            if len(row) == 4:
                cc = TranspositionCipher.from_specification(str(row[0]) + "/" + str(row[1]))
                assert cc.encrypt(bytearray(row[2], "utf-8")) == bytearray(row[3], "utf-8")
                assert cc.decrypt(cc.encrypt(bytearray(row[2], "utf-8"))) == bytearray(row[2], "utf-8")
            elif len(row) == 3:
                cc = TranspositionCipher.from_specification(str(row[0]) + "/" + str(row[1]))
                assert cc.decrypt(cc.encrypt(bytearray(row[2], "utf-8"))) == bytearray(row[2], "utf-8")


if __name__ == '__main__':
    unittest.main()
