from receiver import Receiver
from sender import Sender 
from aescipher import AESCipher
from binascii import hexlify
import hashlib

myID = 1234
print("Hello, welcome to our banking system,\nFor receiving funds from the bank, press '1'\nFor receiving money from another customer, press '2'\n" +
		"For sending money to another customer, press '3'\nFor synchronizing customers, press '4'\nTo quit, type in 'exit'");
var  = input("Please enter your selection: ")
while (var != 'exit'):

	print("You entered " + str(var))
	if var == 'exit':
		exit()
	if var == '1':
		print("You chose to receive funds from the bank:")

		ss = input("Enter your token here: ");
		cipher = AESCipher()
		token = bytes.fromhex(ss)


		plain = hexlify(cipher.decrypt(token))
		value = int(plain, 16)
		print(value);
		fio = open("storage_files/balance.txt", "r+")

		lastLine = fio.readlines()[-1]
		lastTransaction = lastLine.rstrip('\n\r').split(',')

		newBalance = int(lastTransaction[0]) + value
		newTransaction = str(newBalance) + ',' + str(value) + '\n'

		fio.write(newTransaction)
		fio.close()
		print("You have successfully deposited $" + str(value) + " to your account,\nyour current balance is $" + str(newBalance) )

		
	elif var == '2':
		print("You chose to receive money from another customer:");
		token = input("Enter your token here: ");
		#myId = input("Enter your id: ");
		myReceiver = Receiver(token, int(myID) );

		myReceiver.recvMoney();

	elif var == '3':
		print("You chose to send money to another customer:");
		#sendID = input("Please enter your wallet ID: ");
		receiverID = input("Please enter your receiver ID: ");
		amount = input("Finally, please enter the amount you would like to send to receiver "+receiverID+ ": ");

		mySender =  Sender(int(myID), receiverID, int(amount))

		token = mySender.sendMoney();
		print("Your token is " + str(token) + ", present it to your receiver.");
	elif var == '4':
		print("You chose to synchronize the users:");

		#sendID = input("Please enter your wallet ID: ");
		receiverID = input("Please enter your receiver ID: ");

		mySender =  Sender(int(myID), receiverID, int(0))

		token = mySender.sendMoney();
		print("Your token is " + str(token));
		
		token = input("Now enter the token you received from the other user: ");
		#token = hexlify(b'a41256731a3ed2b725629023e1201055')
		#myId = input("Enter your id: ");

		myReceiver = Receiver(token, int(myID));

		myReceiver.recvMoney();

	var = input("\n\n\nYour last request was completed, what would you like to do next? \nFor receiving funds from the bank, press '1'\nFor receiving money from another customer, press '2'\n" +
		"For sending money to another customer, press '3'\nFor synchronizing customers, press '4'\nTo quit, type in 'exit'\n")	






