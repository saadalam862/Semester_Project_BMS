# ============================================================
#   BANK MANAGEMENT SYSTEM
#   Simple Python OOP Project (Beginner Level)
#   No external database — data stored in memory (lists/dicts)
# ============================================================


# ──────────────────────────────────────────────────────────
#  OOP CONCEPT 1: CLASS & OBJECT
#  A class is a blueprint. An object is a real instance of it.
#  Here, 'BankAccount' is the class (blueprint for every account)
# ──────────────────────────────────────────────────────────

class BankAccount:

    # ── OOP CONCEPT 2: CONSTRUCTOR (__init__)
    # __init__ runs automatically when we create a new account object.
    # It sets the starting values (name, balance, PIN) for each account.
    def __init__(self, account_number, holder_name, pin, balance=0):
        self.account_number = account_number   # public attribute
        self.holder_name    = holder_name      # public attribute
        self.balance        = balance          # public attribute

        # ── OOP CONCEPT 3: ENCAPSULATION
        # We use a single underscore _ to mark PIN as "private/protected".
        # It should NOT be accessed directly from outside the class.
        # Instead, we use the check_pin() method to verify it safely.
        self._pin = pin

    # ── OOP CONCEPT 3 (continued): ENCAPSULATION
    # This method gives controlled access to the private _pin.
    # Outside code never sees the PIN directly — it just gets True/False.
    def check_pin(self, entered_pin):
        return self._pin == entered_pin

    # ── OOP CONCEPT 4: METHOD (Behavior of an object)
    # Methods define what an object CAN DO.
    def deposit(self, amount):
        if amount <= 0:
            print("  [!] Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"  OK  PKR {amount} deposited. New Balance: PKR {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("  [!] Amount must be positive.")
            return
        if amount > self.balance:
            print("  [!] Insufficient balance!")
            return
        self.balance -= amount
        print(f"  OK  PKR {amount} withdrawn. New Balance: PKR {self.balance}")

    # ── OOP CONCEPT 5: __str__ (Object Representation)
    # This special method controls what prints when we do print(account).
    def __str__(self):
        return (
            f"\n  {'='*35}\n"
            f"  Account No : {self.account_number}\n"
            f"  Name       : {self.holder_name}\n"
            f"  Balance    : PKR {self.balance}\n"
            f"  Type       : {self.account_type()}\n"
            f"  {'='*35}"
        )

    # ── OOP CONCEPT 6: METHOD OVERRIDING setup
    # This method returns the account type. Each child class will
    # override this to return its own type name. (see below)
    def account_type(self):
        return "Standard Account"


# ──────────────────────────────────────────────────────────
#  OOP CONCEPT 6: INHERITANCE
#  SavingsAccount INHERITS from BankAccount.
#  It gets all the methods of BankAccount for FREE,
#  and adds its own special feature: interest.
# ──────────────────────────────────────────────────────────

class SavingsAccount(BankAccount):

    # Interest rate — shared by ALL savings accounts
    # This is a CLASS VARIABLE (same for every object of this class)
    INTEREST_RATE = 0.06   # 6%

    # ── We call super().__init__() to run the parent class constructor
    def __init__(self, account_number, holder_name, pin, balance=0):
        super().__init__(account_number, holder_name, pin, balance)

    # ── OOP CONCEPT 7: METHOD OVERRIDING (Polymorphism)
    # We OVERRIDE account_type() from the parent class.
    # Same method name, but different behavior for SavingsAccount.
    def account_type(self):
        return "Savings Account"

    # Extra feature only for SavingsAccount
    def apply_interest(self):
        interest = self.balance * self.INTEREST_RATE
        self.balance += interest
        print(f"  OK  Interest PKR {interest:.2f} added. Balance: PKR {self.balance:.2f}")


# ──────────────────────────────────────────────────────────
#  OOP CONCEPT 6 (continued): INHERITANCE
#  CurrentAccount also inherits from BankAccount.
#  It overrides withdraw() to allow overdraft (extra limit).
# ──────────────────────────────────────────────────────────

class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 10000  # Can go PKR 10,000 below zero

    def __init__(self, account_number, holder_name, pin, balance=0):
        super().__init__(account_number, holder_name, pin, balance)

    # ── OOP CONCEPT 7: METHOD OVERRIDING (Polymorphism)
    # withdraw() is overridden here to allow overdraft.
    # SAME method name as parent, but DIFFERENT behavior.
    def withdraw(self, amount):
        if amount <= 0:
            print("  [!] Amount must be positive.")
            return
        if amount > self.balance + self.OVERDRAFT_LIMIT:
            print(f"  [!] Exceeds overdraft limit of PKR {self.OVERDRAFT_LIMIT}.")
            return
        self.balance -= amount
        print(f"  OK  PKR {amount} withdrawn. New Balance: PKR {self.balance}")

    # ── OOP CONCEPT 7: METHOD OVERRIDING
    def account_type(self):
        return "Current Account"


# ──────────────────────────────────────────────────────────
#  OOP CONCEPT 8: ABSTRACTION
#  The Bank class hides the complex internal logic.
#  The user (menu) just calls simple methods like
#  bank.deposit() without knowing HOW it works inside.
# ──────────────────────────────────────────────────────────

class Bank:

    def __init__(self, name):
        self.name     = name
        # We store all accounts in a simple dictionary
        # Key = account number, Value = account object
        self.accounts = {}
        self.next_acc = 1001   # auto-increment account numbers

    # ── Internal helper — prefixed with _ (not for outside use)
    def _find_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    # ── OOP CONCEPT 8: ABSTRACTION
    # create_account() hides the details of how an account is made.
    # The menu just calls it with simple inputs.
    def create_account(self, name, pin, acc_type):
        acc_no = self.next_acc
        self.next_acc += 1

        # ── OOP CONCEPT 1 (Object Creation)
        # Here we CREATE OBJECTS from our classes based on account type.
        if acc_type == "1":
            account = SavingsAccount(acc_no, name, pin)
        else:
            account = CurrentAccount(acc_no, name, pin)

        self.accounts[acc_no] = account
        print(f"\n  OK  Account created! Account Number: {acc_no}")
        print(account)

    def deposit(self, acc_no, pin, amount):
        account = self._find_account(acc_no)
        if not account:
            print("  [!] Account not found.")
            return
        # ── ENCAPSULATION: using check_pin() instead of reading _pin directly
        if not account.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        account.deposit(amount)

    def withdraw(self, acc_no, pin, amount):
        account = self._find_account(acc_no)
        if not account:
            print("  [!] Account not found.")
            return
        if not account.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        # ── OOP CONCEPT 7: POLYMORPHISM in action
        # We call the SAME method withdraw() on any account.
        # Python automatically calls the RIGHT version:
        #   SavingsAccount  => strict balance check
        #   CurrentAccount  => allows overdraft
        account.withdraw(amount)

    def check_balance(self, acc_no, pin):
        account = self._find_account(acc_no)
        if not account:
            print("  [!] Account not found.")
            return
        if not account.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        print(f"\n  Balance: PKR {account.balance}")

    def show_details(self, acc_no, pin):
        account = self._find_account(acc_no)
        if not account:
            print("  [!] Account not found.")
            return
        if not account.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        print(account)   # calls __str__ automatically

    def apply_interest(self, acc_no, pin):
        account = self._find_account(acc_no)
        if not account:
            print("  [!] Account not found.")
            return
        if not account.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        # isinstance() checks if the object belongs to a class — an OOP feature
        if isinstance(account, SavingsAccount):
            account.apply_interest()
        else:
            print("  [!] Interest only applies to Savings Accounts.")

    def transfer(self, from_acc, pin, to_acc, amount):
        sender   = self._find_account(from_acc)
        receiver = self._find_account(to_acc)
        if not sender:
            print("  [!] Your account not found.")
            return
        if not receiver:
            print("  [!] Recipient account not found.")
            return
        if not sender.check_pin(pin):
            print("  [!] Wrong PIN.")
            return
        if amount > sender.balance:
            print("  [!] Insufficient balance for transfer.")
            return
        sender.balance   -= amount
        receiver.balance += amount
        print(f"  OK  PKR {amount} transferred to {receiver.holder_name}.")

    def show_all_accounts(self):
        if not self.accounts:
            print("  No accounts yet.")
            return
        print(f"\n  {'='*50}")
        print(f"  {'ACC NO':<10} {'NAME':<18} {'TYPE':<18} BALANCE")
        print(f"  {'='*50}")
        for acc in self.accounts.values():
            print(f"  {acc.account_number:<10} {acc.holder_name:<18} {acc.account_type():<18} PKR {acc.balance}")
        print(f"  {'='*50}")


# ──────────────────────────────────────────────────────────
#  MENU  — Simple CLI
# ──────────────────────────────────────────────────────────

# ── OOP CONCEPT 1: Creating an OBJECT of the Bank class
my_bank = Bank("National Bank of Pakistan")


def main():
    print(f"\n{'='*40}")
    print(f"  Welcome to {my_bank.name}")
    print(f"{'='*40}")

    while True:
        print("""
  ------- MAIN MENU --------
  1. Create New Account
  2. Deposit Money
  3. Withdraw Money
  4. Check Balance
  5. Account Details
  6. Transfer Money
  7. Apply Interest (Savings)
  8. Show All Accounts
  0. Exit
  --------------------------""")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  -- Create Account --")
            name  = input("  Name      : ").strip()
            pin   = input("  Set PIN   : ").strip()
            print("  1 = Savings   2 = Current")
            atype = input("  Type      : ").strip()
            my_bank.create_account(name, pin, atype)

        elif choice == "2":
            acc = int(input("\n  Account No : "))
            pin = input("  PIN        : ")
            amt = int(input("  Amount     : PKR "))
            my_bank.deposit(acc, pin, amt)

        elif choice == "3":
            acc = int(input("\n  Account No : "))
            pin = input("  PIN        : ")
            amt = int(input("  Amount     : PKR "))
            my_bank.withdraw(acc, pin, amt)

        elif choice == "4":
            acc = int(input("\n  Account No : "))
            pin = input("  PIN        : ")
            my_bank.check_balance(acc, pin)

        elif choice == "5":
            acc = int(input("\n  Account No : "))
            pin = input("  PIN        : ")
            my_bank.show_details(acc, pin)

        elif choice == "6":
            frm = int(input("\n  Your Account No      : "))
            pin = input("  PIN                  : ")
            to  = int(input("  Recipient Account No : "))
            amt = int(input("  Amount     : PKR     "))
            my_bank.transfer(frm, pin, to, amt)

        elif choice == "7":
            acc = int(input("\n  Account No : "))
            pin = input("  PIN        : ")
            my_bank.apply_interest(acc, pin)

        elif choice == "8":
            my_bank.show_all_accounts()

        elif choice == "0":
            print("\n  Goodbye! Thanks for using PyBank.\n")
            break

        else:
            print("\n  [!] Invalid choice. Try again.")


if __name__ == "__main__":
    main()