
# Custom Exception

class InsufficientBalanceError(Exception):
    """Raised when withdrawal or transfer amount exceeds available balance"""
    pass



# BankAccount Class

class BankAccount:

    def __init__(self, account_number: str, holder_name: str, balance: float, pin: int):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = float(balance)   
        self.__pin = pin                

   
    # Property: Read-only Balance
   
    @property
    def balance(self):
        return self.__balance

   
    # Private Method: Log Transaction
   
    def __log_transaction(self, message: str):
        with open("Transaction_history.txt", "a") as file:
            file.write(message + "\n")

   
    # Deposit Method
   
    def deposit(self, amount: float, pin: int):
        if pin != self.__pin:
            print("Invalid PIN!")
            return

        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Rs {amount} deposited successfully.")
        print(f"Updated Balance: Rs {self.__balance}")

        self.__log_transaction(
            f"Deposit | Account: {self.account_number} | Amount: Rs {amount} | Balance: Rs {self.__balance}"
        )

   
    # Withdraw Method
   
    def withdraw(self, amount: float, pin: int):
        if pin != self.__pin:
            print("Invalid PIN!")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            raise InsufficientBalanceError("Withdrawal amount exceeds balance.")

        self.__balance -= amount
        print(f"Rs {amount} withdrawn successfully.")
        print(f"Remaining Balance: Rs {self.__balance}")

        self.__log_transaction(
            f"Withdraw | Account: {self.account_number} | Amount: Rs {amount} | Balance: Rs {self.__balance}"
        )

   
    # Transfer Method
   
    def transfer(self, target_account, amount: float, pin: int):
        if pin != self.__pin:
            print("Invalid PIN!")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if amount > self.__balance:
            raise InsufficientBalanceError("Transfer amount exceeds balance.")

        self.__balance -= amount
        target_account.__balance += amount

        print(f"Rs {amount} transferred to {target_account.account_number}")
        print(f"Your Remaining Balance: Rs {self.__balance}")

        self.__log_transaction(
            f"Transfer Sent | From: {self.account_number} | To: {target_account.account_number} | "
            f"Amount: Rs {amount} | Balance: Rs {self.__balance}"
        )

        target_account.__log_transaction(
            f"Transfer Received | From: {self.account_number} | To: {target_account.account_number} | "
            f"Amount: Rs {amount} | Balance: Rs {target_account.__balance}"
        )

   
    # String Representation
   
    def __str__(self):
        return f"Account({self.account_number}) | Holder: {self.holder_name} | Balance: Rs {self.__balance}"



# Usage Example

if __name__ == "__main__":

    try:
        acc1 = BankAccount("12345", "Rohit", 10000, 1111)
        acc2 = BankAccount("67890", "Amit", 5000, 2222)

        acc1.deposit(2000, 1111)
        acc1.withdraw(3000, 1111)
        acc1.transfer(acc2, 2000, 1111)

        print("\nFinal Balance:", acc1.balance)

    except InsufficientBalanceError as e:
        print("Transaction Failed:", e)