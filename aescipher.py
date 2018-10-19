from Crypto.Cipher import AES

class AESCipher():

	def __init__(self):
		self.key = bytes.fromhex("752EF0D8FB4958670DBA40AB1F3C1D0F8FB4958670DBA40AB1F3752EF0DC1D0F") 

	def encrypt(self, plainText):
		cipher = AES.new(self.key, AES.MODE_ECB)
		cipherText = cipher.encrypt(plainText)
		return cipherText

	def decrypt(self, cipherText):
		aes = AES.new(self.key, AES.MODE_ECB)
		plainText = aes.decrypt(cipherText)
		return plainText
