from crypto.cipher.cipher import Cipher
from crypto.cipher.alphabet import Alphabet


class CaesarCipher(Cipher):

    def __init__(self, spec):
        key, plain_range, cipher_range = spec.split("/")
        self.alphabet = Alphabet(plain_range, cipher_range)
        try:
            self.key = int(key)
        except ValueError:
            raise Exception("Key should be int")
        if len(self.alphabet.plain_alphabet) != len(
                self.alphabet.cipher_alphabet):
            raise Exception("Length of both alphabet arrays not equal")

    def encode_shift(self, ch, key):
        plain_alphabet = self.alphabet.plain_alphabet
        cipher_alphabet = self.alphabet.cipher_alphabet
        if ord(ch) not in plain_alphabet:
            return ord(ch)
        while key < 0:
            key += len(plain_alphabet)
        return cipher_alphabet[
            (plain_alphabet.index(ord(ch)) + key) % len(plain_alphabet)]

    def decode_shift(self, ch, key):
        plain_alphabet = self.alphabet.plain_alphabet
        cipher_alphabet = self.alphabet.cipher_alphabet
        if ord(ch) not in cipher_alphabet:
            return ord(ch)
        while key < 0:
            key += len(cipher_alphabet)
        return plain_alphabet[(cipher_alphabet.index(ord(ch)) +
                    len(cipher_alphabet) - key) % len(cipher_alphabet)]


    def encrypt(self, text):
        if not isinstance(text, str):
            return text
        encrypted = ""
        for c in text:
            x = self.encode_shift(c, self.key)
            print(x)
            encrypted += chr(x)
        return encrypted


    def decrypt(self, text):
        if not isinstance(text, str):
            return text
        decrypted = ""
        for c in text:
            decrypted += chr(self.decode_shift(c, self.key))
        return decrypted


if __name__ == '__main__':
    cc = CaesarCipher("45/azAZ09/azAZ09")
    print(cc.alphabet.plain_alphabet)
    print(cc.alphabet.cipher_alphabet)
    print(cc.encrypt('None9👍'))
    print(CaesarCipher("2/azAZ/azAZ").encrypt("None9👍"))
    cs = CaesarCipher('5/AZaz09/AZaz09')
    print(cs.decrypt(cs.encrypt('abc')))
