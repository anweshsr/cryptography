import math
import numpy as np

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
        assert key > 0
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

    def encrypt_bytes_basic(self, barray: bytearray, key: int) -> bytearray:
        ciphertext = [b''] * key
        for col in range(key):
            currentIndex = col
            while currentIndex<len(barray):
                ciphertext[col] += bytes(barray[currentIndex])
                currentIndex += key
        return bytearray(b''.join(ciphertext))

    def encrypt_bytes_numpy(self, barray: bytearray, key: int) -> bytearray:
        """
        Encrypts a bytearray using numpy functions
        :param barray: bytearray, The byte array to be encrypted
        :param key: int, The key which is used to encrypt the bytearray
        :return: Encrypted bytes
        """
        nparray = np.frombuffer(barray, dtype=np.uint8)
        row = int(math.ceil(len(barray)/key))
        diff = row*key - len(barray)
        nparray = np.append(nparray, diff * [ord(self.null_word)])
        nparray = nparray.astype(np.uint8)
        matrix = nparray.reshape((row, key))
        transpose_mat = matrix.transpose()
        return transpose_mat.tobytes()

    def encrypt(self, barray: bytearray) -> bytearray:
        """
        Encrypts a byte array
        :param text: bytearray, The byte array to be encrypted
        :return: Encrypted bytes
        """
        key = self.key
        encrypted_bytes = self.encrypt_bytes_numpy(barray, key)
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

    def decrypt_bytes_basic(self, barray: bytearray, key: int) -> bytearray:
        col = int(math.ceil(len(barray)/float(key)))
        row = key
        diff = (col * row) - len(barray)
        plaintext = [b''] * col
        i, j = 0, 0
        for char in barray:
            plaintext[i]+=char
            i+=1
            if (i==col) or (i==col-1 and j>=row - diff):
                i=0
                j+=1
        return bytearray(b'').join(plaintext)

    def decrypt_bytes_numpy(self, barray: bytearray, key: int) -> bytearray:
        nparray = np.frombuffer(barray, dtype=np.uint8)
        row = key
        col = int(math.ceil(len(nparray)/row))
        matrix = nparray.reshape((row, col))
        transpose_mat = matrix.transpose()
        transpose_mat = transpose_mat.flatten()
        transpose_mat = np.delete(transpose_mat, np.where(transpose_mat == ord(self.null_word)))
        return bytearray(transpose_mat.tobytes())

    def decrypt(self, barray: bytearray) -> bytearray:
        """
        Decrypts a bytearray object
        :param text: bytearray
        :return:
        """
        key = self.key
        decrypted_bytes = self.decrypt_bytes_numpy(barray, key)
        return decrypted_bytes

if __name__ == '__main__':
    tc = TranspositionCipher(130, "$")
    print(tc.encrypt(bytearray("1234567898", "utf-8")))
    print(tc.decrypt(bytearray("", "utf-8")))
    print(tc.decrypt(tc.encrypt(bytearray("hello world!", "utf-8"))))