from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self,keytext,ivtext) :
        hash = SHA.new() 
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]

    def makeEnabled(self, plaintext) :
        fillersize = 0
        textsize = len(plaintext)
        if textsize%16 != 0 :
            fillersize = 16 - textsize% 16

        filler  = '0'*fillersize
        header = '%d' %(fillersize)
        gap = 16 - len(header)

        header += '#'*gap
        return header+plaintext+filler

    def enc(self , plaintext) : 
        plaintext = self.makeEnabled(plaintext)
        aes = AES.new(self.key,AES.MODE_CBC,self.iv)
        enmsg=aes.encrypt(plaintext)
        return enmsg
        
    def dec(self,ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC,self.iv)
        demsg = aes.decrypt(ciphertext)

        header = demsg[:16].decode()
        fillersize = int(header.split('#')[0])
        
        if fillersize != 0 :
            demsg = demsg[16:-fillersize]
        else:
            demsg=demsg[16:]
        return demsg

def main() :
    keytext = 'Hello'
    ivtext  = '123456'
    msg = 'python3x'

    myCipher = myAES(keytext,ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)

    print('Origin : %s' % msg)
    print('Cipher : %s' % ciphered)
    print('Decipher : %s' % deciphered)

main()