from aescipher import AESCipher
from pathlib import Path
import binascii

class Sender():

	def __init__(self, sendID, recvID, amount):
		self.sendID = sendID
		self.recvID = recvID
		self.amount = amount
		self.counter = 0

		if(self.amount == 0):
			self.isSynchToken = True
		else:
			self.isSynchToken = False

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

	def sendMoney(self):
		token = self._getToken()
		
		# Update Balance
		if(not self.isSynchToken):
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
		contents = Path("storage_files/counter.txt").read_text()
		contents = contents.split(';\n')

		walletID = contents[0].split(',')
		counters = contents[1].split(',')
		
		recvID = str(self.recvID)
		if(recvID in walletID):
			indexID = walletID.index(recvID)

			if(self.isSynchToken):
				counters[indexID] = str(self.counter + 1)
			else:
				counters[indexID] = str(int(counters[indexID]) + 1)
		else:
			walletID.append(recvID)	
			counters.append(str(self.counter + 1))

		idString = (','.join(walletID) + ';\n')
		ctrString = (','.join(counters))

		try:
			fioc = open("storage_files/counter.txt", "w")
			fioc.write(idString)
			fioc.write(ctrString)
			fioc.close()	
		except FileNotFoundError:
			print("Wrong file or file path")	

		return binascii.hexlify(token)