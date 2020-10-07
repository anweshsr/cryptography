from crypto.cipher.cipher import Cipher

class ReverseCipher(Cipher):

    def _reverse(self, text):
        if isinstance(text, str) or isinstance(text, bytes):
            return text[::-1]
        return text

    def encrypt(self, text):
        return self._reverse(text)

    def decrypt(self, text):
        return self._reverse(text)

if __name__ == '__main__':
    rc = ReverseCipher()
    #print(rc.encrypt(b'None9👍'))
    print(rc.encrypt(bytes('None9👍'.encode())))
    print(bytearray('None9👍'.encode('utf-8')))