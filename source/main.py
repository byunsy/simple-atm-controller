"""============================================================================
TITLE      : main.py
AUTHOR     : Sang Yoon Byun

DESCRIPTION: This is the main program for the ATM Controller project. While it
             does not integrate with a real bank system, it has basic features
             like inserting a card, putting PIN numbers, selecting an account 
             (checking or savings), displaying current balance, depositing, and
             withdrawing money.  
============================================================================"""

from time import sleep
import atm_display as dp
import atm_controller as ac


"""----------------------------------------------------------------------------
                                     MAIN
----------------------------------------------------------------------------"""
def main():

    while True:

        # Clear screen
        dp.clear()

        # Show main ATM menu
        dp.show_menu()
        print()
        
        # User Input
        option = input("Select Option: ")

        ### CREATE ACCOUNT ================================================ ###
        if option == '1':

            dp.show_banner("Creating Account")
            ac.make_account()
        
        ### INSERT CARD =================================================== ###
        elif option == '2':

            dp.show_banner("Insert Card")
            success, idx = ac.verification()
            sleep(2)
            
            # If card successfully verified with PIN number
            if success:

                while True:
                    dp.clear()
                    dp.show_account_menu()
                    ac.show_account_info(idx)
                    option = input("Select Option: ")

                    ### CHECKING ACCOUNT ================================== ###
                    if option == '1':
                        
                        while True:
                            dp.clear()
                            dp.show_account_actions()
                            option = input("Select Action: ")

                            if option == "1":
                                ac.show_balance(idx, 'c')
                            elif option == "2":
                                ac.deposit_money(idx, 'c')
                            elif option == "3":
                                ac.withdraw_money(idx, 'c')
                            elif option == '4':
                                break
                            else:
                                print("Please choose a number from the menu above.")
                                sleep(1)

                    ### SAVINGS ACCOUNT =================================== ###
                    elif option == '2':

                        while True:
                            dp.clear()
                            dp.show_account_actions()
                            option = input("Select Action: ")

                            if option == "1":
                                ac.show_balance(idx, 's')
                            elif option == "2":
                                ac.deposit_money(idx, 's')
                            elif option == "3":
                                ac.withdraw_money(idx, 's')
                            elif option == '4':
                                break
                            else:
                                print("Please choose a number from the menu above.")
                                sleep(1)

                    ### EXIT ============================================== ###
                    elif option == '3':
                        dp.clear()
                        print("\n\n")
                        dp.print_center("Please take your card.\n\n")
                        dp.print_center("Thank you for choosing Bear Bank.\n\n")
                        sleep(3)
                        break

                    else:
                        print("Please choose a number from the menu above.")
                        sleep(1)
            
            else:
                continue

        elif option == '3':
            print("\nEnd of Program.")
            sleep(1)
            dp.clear()
            break

        else:
            print("Please choose a number from the menu above.")
            sleep(1)


if __name__ == '__main__':
    main()