from aescipher import AESCipher
import binascii

class Sender():

	def __init__(self, sendID, recvID, amount):
		self.sendID = sendID
		self.recvID = recvID
		self.amount = amount
		self.counter = 0

	def _concatenateInfo(self):

		sendID = str(self.sendID).zfill(4)
		recvID = str(self.recvID).zfill(4)
		amount = str(self.amount).zfill(4)
		counter = str(self.counter).zfill(4)
		
		return sendID + recvID + amount + counter

	def _getToken(self):
		cipher = AESCipher()

		plainToken = self._concatenateInfo()
		cipherToken = cipher.encrypt(plainToken)

		return cipherToken

	def _getCounter(self):

		# TODO:
		# Open file and get associated counter

		return

	def sendMoney(self):
		token = self._getToken()
		
		# Update Balance
		if(self.amount != 0):
			try:
				fio = open("storage_files/balance.txt", "r+")

				lastLine = fio.readlines()[-1]
				lastTransaction = lastLine.rstrip('\n\r').split(',')

				newBalance = int(lastTransaction[0]) - self.amount
				newTransaction = str(newBalance) + ',' + str(self.amount) + '\n'

				fio.write(newTransaction)
				fio.close()
			except FileNotFoundError:
				print("Wrong file or file path")	

		
		# Update Counter

		return binascii.hexlify(token)