# project 1: ATM Machine simulation 💳

balance = 1000

print("welcome to ATM!")

print("1.check balance")
print("2.witdraw money")
print("3.deposit money")

option = int(input("chose an option(1-3: " ))

if option == 1:
   print("your current balance is RS.", balance)

elif option == 2:
   witdraw = int(input("enter amount to witdraw: "))
   if witdraw <= balance:
      balance -= witdraw
      print("witdraw successful!")
      print("new balance is:", balance)
   else:
      print("insuffiecient amount!")

elif option == 3:
   deposit = int(input("enter amount to deposit: "))
   balance += deposit
   print("deposit successful!")
   print("new balance is:", balance)

else:
   print("invalid option! please choose 1 to 3.")