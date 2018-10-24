from aescipher import AESCipher
from pathlib import Path
from binascii import unhexlify

class Receiver():

	# myID is in integers
	def __init__(self, token, myID):
		self.token = unhexlify(token)
		self.myID = myID
		self.verified = False

		plainToken = str(self._getPlainToken(), 'utf-8')
		self._getInfo(plainToken)
		print(plainToken)

		if(self.amount == 0):
			self.isSynchToken = True
		else:
			self.isSynchToken = False

	def _getInfo(self, plainToken):

		self.sendID = int(plainToken[:4].lstrip('0'))
		self.recvID = int(plainToken[4:8].lstrip('0'))
		amount = plainToken[8:12]
		if(amount == '0000'):
			self.amount = 0
		else:
			self.amount = int(amount.lstrip('0'))
		counter = plainToken[12:16]
		if(counter == '0000'):
			self.counter = 0
		else:
			self.counter = int(counter.lstrip('0'))
	
		return 

	def _getPlainToken(self):
		cipher = AESCipher()

		plainToken = cipher.decrypt(self.token)

		return plainToken

	def _verifyIDCounter(self, counter):
		return (self.recvID == self.myID) and (counter == self.counter)

	def _updateCounter(self):
		contents = Path("storage_files/counter.txt").read_text()
		contents = contents.split(';\n')

		walletID = contents[0].split(',')
		counters = contents[1].split(',')

		sendID = str(self.sendID)
		if(sendID in walletID):
			indexID = walletID.index(sendID)

			if(self._verifyIDCounter(int(counters[indexID]))):
				self.verified = True
				counters[indexID] = str(self.counter + 1)	
			else:
				self.verified = False
		else:	
			if(self.isSynchToken and (self.recvID == self.myID)):
				walletID.append(sendID)	
				counters.append(str(self.counter + 1))	
				self.verified = True
			else:
				self.verified = False

		if(self.verified):
			idString = (','.join(walletID) + ';\n')
			ctrString = (','.join(counters))

			try:
				fioc = open("storage_files/counter.txt", "w")
				fioc.write(idString)
				fioc.write(ctrString)
				fioc.close()	
			except FileNotFoundError:
				print("Wrong file or file path")

			return True
		else:
			return False
				
	def _updateBalance(self):
		if(not self.isSynchToken):
			try:
				fio = open("storage_files/balance.txt", "r+")

				lastLine = fio.readlines()[-1]
				lastTransaction = lastLine.rstrip('\n\r').split(',')

				newBalance = int(lastTransaction[0]) + self.amount
				newTransaction = str(newBalance) + ',' + str(self.amount) + '\n'

				fio.write(newTransaction)
				fio.close()
			except FileNotFoundError:
				print("Wrong file or file path")

		return

	def recvMoney(self):
		
		if(self._updateCounter()):
			print('Wallet updated.')

			self._updateBalance()

			return True
		else:
			print('Something went wrong.')	

			return False