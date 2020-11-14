import math

from cipher.cipher import Cipher

def chunks(lst, n):
    """
    Generator which breaks a list into sublists of length n
    :param lst: list
    :param n: int
    :return:
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def transpose(l1, l2):
    """
    Given a matrix as a list of lists, returns the transpose of the matrix
    :param l1: list
    :param l2: empty list
    :return: list
    """
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

def create_matrix(bytestring, key):
    """
    Given a byte string breaks the bytestring into chunks of even length and
    creates a matrix as a list of lists
    :param bytestring:
    :param key:
    :return:
    """
    l = []
    for byte in bytestring:
        l.append(byte)
    matrix = list(chunks(l, key))
    return matrix

class TranspositionCipher(Cipher):
    """
    This engine implements the Transposition Cipher algorithm given a valid key
    Example: if key is 3 1234567898 will become 1478258$369$ where $ is the null
    word
    """
    def __init__(self, key, null_word):
        assert type(key) == int
        self.key = key
        self.null_word = null_word

    @classmethod
    def from_specification(cls, spec):
        specs = spec.split("/")
        key = int(specs[0])
        null_word = specs[1] if len(specs) == 2 else "$"
        return cls(key, null_word)

    def encrypt_bytes(self, bytestring, key):
        matrix = create_matrix(bytestring, key)
        if len(matrix[-1]) < key:
            diff = key - len(matrix[-1])
            matrix[-1] = matrix[-1] + diff * [None]
        transpose_mat = transpose(matrix, [])
        xs = bytearray()
        flatten = [item for sublist in transpose_mat for item in sublist]
        for i in flatten:
            byte = ord(self.null_word) if not i else i
            xs.append(byte)
        return xs

    def encrypt(self, text, return_type=None):
        """
        Takes bytes, string, bytearray and encrypts it
        :param text: (bytes, str, bytearray)
        :param return_type: str or None
        :return: str or bytearray
        """
        if not isinstance(text, (str, bytearray, bytes)):
            return text
        key = self.key
        bytestring = bytearray(text, "utf-8") if type(text)==str else bytearray(text)
        encrypted_bytes = self.encrypt_bytes(bytestring, key)
        if return_type==str:
            encrypted_bytes = encrypted_bytes.decode("utf-8")
        return encrypted_bytes

    def decrypt_bytes(self, text, key):
        text_len = float(len(text))
        key = self.key
        col = key
        row = int(math.ceil(text_len/col))
        mat = create_matrix(text, row)
        transpose_mat = transpose(mat, [])
        flatten = [item for sublist in transpose_mat for item in sublist]
        byte_list = list(filter(lambda x: x != ord(self.null_word), flatten))
        xs = bytearray()
        for byte in byte_list:
            xs.append(byte)
        return xs

    def decrypt(self, text, return_type=None):
        """
        Decrypts a string or bytearray or bytes into string
        :param text: (string, bytearray, bytes)
        :param return_type: str or None
        :return:
        """
        if not isinstance(text, (str, bytearray, bytes)):
            return text
        key = self.key
        bytestring = bytearray(text, "utf-8") if type(text)==str else bytearray(text)
        decrypted_bytes = self.decrypt_bytes(bytestring, key)
        if return_type==str:
            decrypted_bytes = decrypted_bytes.decode("utf-8")
        return decrypted_bytes

if __name__ == '__main__':
    tc = TranspositionCipher(3, "$")
    print(tc.encrypt("1234567898", return_type=str))
    print(tc.encrypt("1478258$369$"))
    print(tc.decrypt("1478258$369$", return_type=str))