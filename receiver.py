from aescipher import AESCipher

class Receiver():

	def __init__(self, token):
		self.token = token

	def _getInfo(self, plainToken):
		# TODO
		return 'TODOTODOTODOTODO'

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