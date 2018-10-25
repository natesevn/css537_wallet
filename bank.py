from receiver import Receiver
from sender import Sender 
from aescipher import AESCipher
from binascii import hexlify

print("Hello, welcome to our banking system,\nFor receiving funds from the bank, press '1'.\nFor receiving money from another customer, press '2'\n" +
		"For sending money to another customer, press '3'\nFor synchronizing customers, press '4'");
while (1):
	
	var = input("Please enter your selection: ")


	print("You entered " + str(var))
	if var == '1':
		print("You chose to receive funds from the bank.")
		
		amount = input("Please enter the amount: ")
		fio = open("storage_files/balance.txt", "r+")

		newTransaction = str(amount) + ',' + str(amount) + '\n'

		fio.write(newTransaction)
		fio.close()		
		
		
	elif var == '2':
		print("You chose to receive money from another customer.");
		token = input("Enter your token here: ");

		myReceiver = Receiver(token, int(1234) );
		myReceiver.recvMoney();

	elif var == '3':
		print("You chose to send money to another customer.");
		sendID = input("Please enter your wallet ID: ");
		receiverID = input("Please enter your receiver ID: ");
		amount = input("Finally, please enter the amount you would like to send to receiver "+receiverID+ ": ");
		mySender =  Sender(sendID, receiverID, amount)
		token = mySender.sendMoney();
		print("Your token is: " + str(token));
	else :
		print("You chose to synchornzie the users: ");

		sendID = input("Please enter your Wallet ID: ");
		receiverID = input("Please enter your receiver ID: ");
		mySender =  Sender(sendID, receiverID, int(0))
		token = mySender.sendMoney();
		print("Your token is: " + str(token));
		
		token = input("Now enter the token you received from the other user: ");
		#token = hexlify(b'a41256731a3ed2b725629023e1201055')
		#myId = input("Enter your id: ");
		myReceiver = Receiver(token, int(1234));
		myReceiver.recvMoney();



	todo = input("Your request has completed, choose another transaction or type 'exit' to quit: ");	
	if(todo == 'exit'):
		exit();



