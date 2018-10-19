from aescipher import AESCipher

class Sender():

	def __init__(self, sendID, recvID, amount, counter):
		self.sendID = sendID
		self.recvID = recvID
		self.amount = amount
		self.counter = counter

	def _concatenateInfo(self):
		# TODO
		return 'TODOTODOTODOTODO'

	def _getToken(self):
		cipher = AESCipher()

		plainToken = self._concatenateInfo()
		cipherToken = cipher.encrypt(plainToken)

		return cipherToken

	def sendMoney(self):
		token = self._getToken()
		
		# TODO:
		# Update Balance
		# Update Counter

		return True