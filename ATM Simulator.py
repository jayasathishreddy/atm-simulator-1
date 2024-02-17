#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[10]:


class ATM:
   def __init__(self):
       self.balance = 10000  # Default balance

   def check_balance(self):
       print(f"Your balance is Rs.{self.balance}")

   def withdraw(self, amount):
       if self.balance >= amount:
           self.balance -= amount
           print(f"Withdrawal successful. Remaining balance is Rs.{self.balance}")
       else:
           print("Insufficient balance")

   def deposit(self, amount):
       self.balance += amount
       print(f"Deposit successful. Current balance is Rs.{self.balance}")

   def run(self):
       print("** Welcome To ATM Machine Simulator **")
       pin = input("Enter Your Pin: ")
       if pin != "65566":
           print("Invalid PIN")
           return

       while True:
           print("\nOptions you can Exercise are:")
           print("1) Balance")
           print("2) Withdraw")
           print("3) Deposit")
           print("4) Exit")

           choice = input("Select Your Transaction from the above options: ")

           if choice == "1":
               self.check_balance()
           elif choice == "2":
               amount = float(input("Enter Amount: "))
               self.withdraw(amount)
           elif choice == "3":
               amount = float(input("Enter Amount: "))
               self.deposit(amount)
           elif choice == "4":
               print("Thank you for using the ATM. Goodbye!")
               break
           else:
               print("Invalid choice")


# Instantiate and run the ATM simulator
atm = ATM()
atm.run()


# In[ ]:





# In[ ]:




