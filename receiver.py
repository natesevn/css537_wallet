from aescipher import AESCipher

class Receiver():

	def __init__(self, token):
		self.token = token

	def _getInfo(self, plainToken):

		self.sendID = plainToken[:4].lstrip('0')
		self.walletID = plainToken[4:8].lstrip('0')
		amount = plainToken[8:12]
		if(amount == '0000'):
			self.amount = 0
		else:
			self.amount = amount.lstrip('0')
		counter = plainToken[12:16]
		if(counter == '0000'):
			self.counter = 0
		else:
			self.counter = counter.lstrip('0')
	
		return 

	def _getPlainToken(self):
		cipher = AESCipher()

		plainToken = cipher.decrypt(self.token)

		return plainToken

	def recvMoney(self):
		plainToken = self._getPlainToken()

		# _getInfo stores all retrieved information in self
		self._getInfo()

		# TODO:
		# Verify sender ID
		# Verify counter
		
		# TODO:
		# Update Balance
		# Update Counter

		return True