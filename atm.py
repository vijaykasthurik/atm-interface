print("______________________________________________________________________")
print("\t\t\t CANARA BANK - MADURAI BRANCH")
print("______________________________________________________________________")
print("\t\t\tATM SERVICES")
print("______________________________________________________________________")
user_id=int(input("Enter you User ID :"))
passkey=int(input("Enter your Password :"))
if(user_id==33 and passkey==6382):
	print("______________________________________________________________________")
	print("USER NAME : VIJAY KASTHURI K\nACCOUNT NUMBER : 179238")
	print("______________________________________________________________________")
	balance=5000
	mid=300
	while(True):
		print("Choose you Service\n1.Balance Check\n2.Deposit\n3.Withdrawal\n4.Money Transfer\n5.Quit")
		choice=int(input("Enter your Service:"))
		if(choice==1):
			print("Account Balance : ",balance)
			print("")
		elif(choice==2):
			amt=int(input("Enter the Amount:"))
			balance+=amt
			print("Amount Deposited Successfully")
			print("Account Balance :",balance)
			print("")
		elif(choice==3):
			amt=int(input("Enter the Amount:"))
			if(amt>balance):
				print("Not Enough Balance !")
			else:
				balance-=amt
				print("Amount Withdrawn Successfully")
				print("Account Balance :",balance)
			print("")
		elif(choice==4):
			mid=int(input("Enter the BANK ID number :"))
			amt=int(input("Enter your Amount:"))
			mid+=amt
			balance-=amt
			print("Money Transferred Successfully")
			print("Account Balance :",balance)
			print("")
		elif(choice==5):
			print("Thankyou for visiting !!! Welcome")
			print("")
			break
		else:
			print("Invalid Choice")
else:
	print("No user Details Found")
