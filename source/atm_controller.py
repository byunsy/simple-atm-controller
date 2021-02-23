"""============================================================================
TITLE      : atm_controller.py
AUTHOR     : Sang Yoon Byun
DESCRIPTION: A simple ATM controller with basic features.
============================================================================"""

from time import sleep

# List to store all accounts
accounts_list = []


"""----------------------------------------------------------------------------
CLASS ACCOUNT
----------------------------------------------------------------------------"""
class Account:

    def __init__(self, name, card_num, pin_num):
        self.name = name
        self.card = card_num
        self.pin  = pin_num
        self.c_balance = 0
        self.s_balance = 0

    def get_name(self):
        return self.name

    def get_card_num(self):
        return self.card

    def get_pin_num(self):
        return self.pin

    ### CHECKING ACCOUNT ================================================== ###
    def c_get_balance(self):
        return self.c_balance

    def c_deposit(self, money):
        self.c_balance += int(money)

    def c_withdraw(self, money):
        if self.c_balance < int(money):
            print("Sorry. There is not enough balance in your account.")
            return 0

        self.c_balance -= int(money)
        print("${} successfully withdrawn from your checking account!".format(money))
    
    ### SAVINGS ACCOUNT =================================================== ###
    def s_get_balance(self):
        return self.s_balance

    def s_deposit(self, money):
        self.s_balance += int(money)

    def s_withdraw(self, money):
        if self.s_balance < int(money):
            print("Sorry. There is not enough balance in your account.")
            return 0

        self.s_balance -= int(money)
        print("${} successfully withdrawn from your checking account!".format(money))


"""----------------------------------------------------------------------------
PROCEDURE:
    check_card_num(string)
PARAMETERS:
    string, an input card number in string format
PURPOSE:
    Checks if the input card number is valid.
PRODUCES:
    bool, a True or False value (valid or invalid)
----------------------------------------------------------------------------"""
def check_card_num(input_card):

    # check if it contains '-'
    if '-' not in input_card:
        return False

    # check if it splits into four chucks
    split_num = input_card.split("-")
    if len(split_num) != 4:
        return False

    # check if all chunks are length 4 and numeric
    for num in split_num:
        if not num.isdigit():
            return False

        if len(num) != 4:
            return False
    
    # If it passed all the tests above, return True
    return True


"""----------------------------------------------------------------------------
PROCEDURE:
    check_pin_num(string)
PARAMETERS:
    string, an input PIN number in string format
PURPOSE:
    Checks if the input pin number is valid.
PRODUCES:
    bool, a True or False value (valid or invalid)
----------------------------------------------------------------------------"""
def check_pin_num(input_pin):

    # check if it has length of 6
    if len(input_pin) != 6:
        return False

    # check if all are digits
    if not input_pin.isdigit():
        return False

    # If it passed all the tests above, return True
    return True


"""----------------------------------------------------------------------------
PROCEDURE:
    make_account()
PARAMETERS:
    none
PURPOSE:
    Creates an account and adds it to the system. This step is required for
    users to insert and use their cards. 
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def make_account():

    # Enter Name
    account_name = input("Please enter your name:\n  ")
    print()

    # Enter Card Number
    while True:
        account_card = input("Please enter your card number (eg. OOOO-OOOO-OOOO-OOOO):\n  ")
        if check_card_num(account_card):
            break
        print("Error: Incorrect Format.\n\n")
    print()
    
    # Enter PIN Number
    while True:
        account_pin  = input("Please enter your PIN number (6 digits):\n  ")
        if check_pin_num(account_pin):
            break
        print("Error: Incorrect Format.\n\n")
    print()

    # Add to the list of all accounts
    accounts_list.append(Account(account_name, account_card, account_pin))

    print("Account created successfully!")

    sleep(2)


"""----------------------------------------------------------------------------
PROCEDURE:
    verification()
PARAMETERS:
    none
PURPOSE:
    A simulation of inserting, reading, and verifying a card. Checks if the 
    card number exists in the system, and checks if it matches the PIN number.
PRODUCES:
    bool, whether the card was successfully verified.
    idx, an index of the account found in the accounts_list.
----------------------------------------------------------------------------"""
def verification():

    # Enter card number
    while True:
        input_card = input("Please enter your card number (eg. OOOO-OOOO-OOOO-OOOO):\n  ")
        if check_card_num(input_card):
            break
        print("Error: Incorrect Format.\n\n")
    print()

    # Enter PIN number
    while True: 
        input_pin  = input("Please enter your PIN number (6 digits):\n  ")
        if check_pin_num(input_pin):
            break
        print("Error: Incorrect Format.\n\n")
    print()

    # traverse through all accounts
    for idx in range(len(accounts_list)):

        # if card number and PIN matched in the system
        if accounts_list[idx].get_card_num() == input_card:
            if accounts_list[idx].get_pin_num() == input_pin:
                print("Verified successfully!")
                return True, idx

            # if PIN does not match card number
            else:
                print("Incorrect PIN Number: Does not match your card number.\n\n")
                print("Please try again.")
                sleep(2)
                return False, None

    # if account not found in the system:
    print("Incorrect Card Number: Does not exist in our system.\n\n")
    print("If you have not yet created an account, please proceed to Option 1.")
    sleep(2)

    return False, None


"""----------------------------------------------------------------------------
PROCEDURE:
    show_account_info(idx)
PARAMETERS:
    idx, an index of the account found in the accounts_list.
PURPOSE:
    Shows the overall account information: name, card, checking balance, and
    savings balance.
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_account_info(idx):

        account = accounts_list[idx]

        print("Name:  {}\n\n".format(account.get_name()))
        
        print("Card:  {}-****-****-{}\n\n".format(account.get_card_num()[:4], 
                                                  account.get_card_num()[-4:]))
        
        print("Current Balance [Checking]:  ${}\n\n".format(account.c_get_balance()))
        
        print("Current Balance [Savings] :  ${}\n\n".format(account.s_get_balance()))
        
        print()


"""----------------------------------------------------------------------------
PROCEDURE:
    show_balance(idx, account)
PARAMETERS:
    idx, an index in the accounts_list for selected account
    account, a char value ('c' for checking and 's' for savings)
PURPOSE:
    Displays the current balance of a specified account.
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_balance(idx, account):

    if account == 'c':
        balance = accounts_list[idx].c_get_balance()
        print()
        print("Current Balance [Checking]: {}".format(balance))

    else:
        balance = accounts_list[idx].s_get_balance()
        print()
        print("Current Balance [Savings]: {}".format(balance))
    
    print("\n\n\n")
    _ = input("Press 'Enter' to go back.")


"""----------------------------------------------------------------------------
PROCEDURE:
    deposit_money(idx, account)
PARAMETERS:
    idx, an index in the accounts_list for selected account
    account, a char value ('c' for checking and 's' for savings)
PURPOSE:
    Deposits specified amount of money to an account
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def deposit_money(idx, account):

    print()
    money = input("Select amount to deposit:\n  $ ")
    print()

    if account == 'c':
        accounts_list[idx].c_deposit(money)
        print("${} successfully deposited to your checking account!".format(money))
        sleep(1)

    else:
        accounts_list[idx].s_deposit(money)
        print("${} successfully deposited to your savings account!".format(money))
        sleep(1)


"""----------------------------------------------------------------------------
PROCEDURE:
    withdraw_money(idx, account)
PARAMETERS:
    idx, an index in the accounts_list for selected account
    account, a char value ('c' for checking and 's' for savings)
PURPOSE:
    Withdraws specified amount of money from an account
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def withdraw_money(idx, account):

    print()
    money = input("Select amount to withdraw:\n  $ ")
    print()

    if account == 'c':
        accounts_list[idx].c_withdraw(money)
        sleep(1)

    else:
        accounts_list[idx].s_withdraw(money)
        sleep(1)
        
