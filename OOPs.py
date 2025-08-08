
class BankAccount:
    def __init__(self, amount):
        self.accountNum = self.getValidAccountNum()
        self.amount = amount
        
        
    def checkAccBalance(self):
        print("\n---- Account Balance ----")
        print(f"Account Number : {self.accountNum}")
        print(f"Available Funds: ${self.amount:,}")
        print("--------------------------")


    def getValidAccountNum(self):
        while True:
            try:
                acc = int(input("Enter Account Number (Must be 6 digits): "))
                if len(str(acc)) == 6:
                    return acc
                else:
                    print("Invalid account number. It must be exactly 6 digits.")
            except ValueError:
                print("Please enter numbers only.")
                
    def greetings(self):
        print(f"Welcome, {self.accountNum}")
        

    def AccountNumValidation(self):
        if len(str(self.accountNum)) != 6:
            print("Invalid account number. It must be exactly 6 digits.")
            return False
        return True

    def deposit(self):
        if not self.AccountNumValidation():
            return

        newDeposit = True
        while newDeposit == True:
            try:
                amountToDeposit = int(input(f"How much do you want to deposit?\nEnter amount: "))
                self.amount = self.amount + amountToDeposit
                print(f"\n---- You have successfully deposited ${amountToDeposit:,} ----\n")
                print(f"New account balance: ${self.amount:,}")
                
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
                continue

            anotherDep = input("Do you want to make another deposit? Yes / No?\nEnter: ")
            if anotherDep.lower() == "no":
                newDeposit = False
        print(f"Total in account: ${self.amount:,}")

    def withdraw(self):
        if not self.AccountNumValidation():
            return

        withdrawOptions = [10, 20, 50, 80, 100, 150, 200, 250, 500, 800, 1000, 1500, 2000, 8000, 10000]

        continueWithdrawal = True
        while continueWithdrawal:
            print(f"Choose your withdrawal amount from these: {withdrawOptions}")

            try:
                amountToWithdraw = int(input("How much do you want to withdraw?\nEnter amount: "))
                if amountToWithdraw not in withdrawOptions:
                    print("\nPlease choose a valid withdrawal option.\n")
                    continue
                if amountToWithdraw > self.amount:
                    print("\nERROR. Withdrawal amount exceeds account balance.\n")
                    continue
                self.amount -= amountToWithdraw
                print(f"\n---- Successfully withdrew ${amountToWithdraw:,} ----\n")
                print(f"New account balance: ${self.amount:,}")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
                continue

            anotherWithdrawal = input("Do you want to make another withdrawal? Yes / No?\nEnter: ")
            if anotherWithdrawal.lower() == "no":
                continueWithdrawal = False

  
        
myBank = BankAccount(80710)
myBank.greetings()

while True:
    print("\nHere are the following options you can choose from:")
    print("A: WITHDRAW MONEY   B: DEPOSIT MONEY   C: CHECK ACCOUNT BALANCE   D: EXIT")
    choice = input("ENTER: ").lower()

    if choice in ["withdraw","withdraw money", "a"]:
        myBank.withdraw()
        
    elif choice in ["deposit", "deposit money", "b"]:
        myBank.deposit()
        
    elif choice in ["check account balance", "check balance", "account balance", "c"]:
        myBank.checkAccBalance()
        
    elif choice == "exit" or choice == "d":
        print("\nThank you for banking with us. Goodbye!\n")
        break
    else:
        print("Error!\nInvalid option entered.")
