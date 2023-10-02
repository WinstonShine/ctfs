from Crypto.Cipher import AES
from Crypto import Random

class AESAlg(object):
    def __init__(self, key):
        self.blockSize = 32
        self.key = key

    @staticmethod
    def string_2_bytes(msg):
        a_type = type(b''.decode('utf8'))
        if isinstance(msg, a_type):
            return msg.encode('utf8')
        return msg

    def padding(self, x):
        return x + (self.blockSize - len(x) % self.blockSize) * AESAlg.string_2_bytes(chr(self.blockSize - len(x) % self.blockSize))

    @staticmethod
    def depadding(x):
        return x[:-ord(x[len(x)-1:])]

    def enc(self, pt):
        pt = self.padding(AESAlg.string_2_bytes(pt))
        iv = Random.new().read(16)
        print(len(iv))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pt)

    def dec(self, ct):
        iv = ct[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(ct[AES.block_size:])
