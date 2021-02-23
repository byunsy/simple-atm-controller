"""----------------------------------------------------------------------------
TITLE      : atm_display.py
AUTHOR     : Sang Yoon Byun
DESCRIPTION: A set of basic tools for displaying ATM information.
----------------------------------------------------------------------------"""

from os import system, name 
from time import sleep 
import shutil
  
  
"""----------------------------------------------------------------------------
PROCEDURE:
    clear()
PARAMETERS:
    none
PURPOSE:
    Clears the terminal screen.
PRODUCES:
    none, a void function
REFERENCES:
    https://www.geeksforgeeks.org/clear-screen-python/
----------------------------------------------------------------------------"""
def clear(): 
  
    # for windows system users
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux system users
    else: 
        _ = system('clear') 


"""----------------------------------------------------------------------------
PROCEDURE:
    print_center(string)
PARAMETERS:
    string, any string value
PURPOSE:
    Prints the string at the center of the terminal (in terms of width).
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def print_center(string):

    columns = shutil.get_terminal_size().columns
    print(string.center(columns))


"""----------------------------------------------------------------------------
PROCEDURE:
    show_banner(string)
PARAMETERS:
    string, any string value
PURPOSE:
    Displays a simple banner at the top of the terminal. 
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_banner(string):

    clear()

    print_center("******************")
    print()
    print_center(string)
    print()
    print_center("******************")
    print()


"""----------------------------------------------------------------------------
PROCEDURE:
    show_menu()
PARAMETERS:
    none
PURPOSE:
    Displays the main ATM menu in the beginning.
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_menu():

    print_center("\n\n\n")

    print_center("*************** MENU ***************")
    print()
    print_center("1. Create Account")
    print()
    print_center("2. Insert Card   ")
    print()
    print_center("3. End Program   ")
    print()
    print_center("************************************")


"""----------------------------------------------------------------------------
PROCEDURE:
    show_account_menu()
PARAMETERS:
    none
PURPOSE:
    Displays the account menu when the user has successfully inserted the card.
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_account_menu():

    print_center("\n\n\n")

    print_center("*************** MENU ***************")
    print()
    print_center("1. Checking Account")
    print()
    print_center("2. Savings Account ")
    print()
    print_center("3. Exit            ")
    print()
    print_center("************************************")


"""----------------------------------------------------------------------------
PROCEDURE:
    show_account_actions()
PARAMETERS:
    none
PURPOSE:
    Displays all available account actions for the user to interact with.
PRODUCES:
    none, a void function
----------------------------------------------------------------------------"""
def show_account_actions():

    print_center("\n\n\n")

    print_center("*************** MENU ***************")
    print()
    print_center("1. See Balance")
    print()
    print_center("2. Deposit    ")
    print()
    print_center("3. Withdraw   ")
    print()
    print_center("4. Exit       ")
    print()
    print_center("************************************")

