# simple-atm-controller

## Description

Simple-atm-controller allows users to interact with a terminal-based ATM machine. While the program does not integrate with a real bank system, it has basic and userful features like inserting a card, putting a corresponding PIN number, selecting an account (checking and/or savings), displaying the current balance, depositing, and withdrawing. A user can create an account with his or her choice of name, card number, and PIN number, all of which will be stored. Later on, as users insert their cards, their PIN numbers must match their card number they specified when creating the account.

For simplicity, all account balances were represented as integers and every account user only have two accounts--checking and savings. Users are also not able to transfer money or withdraw more than their total balance. Moreover, since the users cannot actually 'insert' their cards, I have decided to simulate it instead by typing in their card numbers in the 'Insert Cards' action.

## Basic Instructions

The program have four main steps.

1. Create Account

   - Before you insert your card, make sure that you have actually created an account using the ATM. Creating the account will require you to input your name, card number (XXXX-XXXX-XXXX-XXXX format), and PIN number (6 digits).
   - The information you pass in will be stored within the program. Make sure you remember the information you type in.

2. Insert Card

   - You will be able to 'insert' your card by passing in your card number (so that the program can read the card information).
   - Card number must be typed in as XXXX-XXXX-XXXX-XXXX 16 digit format.

3. PIN number

   - Afterwards, you will need to type in the PIN number you have registered with. The program will check whether your PIN number matches the card number.
   - PIN number must be six digits without any spaces or characters in between.

4. Select Account

   - You can select Checkings and/or Savings account.

5. Selcet Action (See Balance/Deposit/Withdraw)

   - You will have a total of three account actions: See Balance, Deposit, and Withdraw).
   - 'See Balance' will display the current balance of the account you have selected. 'Deposit' and 'Withdraw' will ask you to specify the amount you would like to deposit to and/or withdraw from your account.

## Installation

No additional installations are required for this repository besides Python.

Make sure you are using Python 3 versions (I personally used Python 3.7.2).

## Usage

Clone the simple-atm-controller repository in your directory.

```bash
git clone https://github.com/byunsy/simple-atm-controller
```

Make sure you are using the correct version of Python.

```bash
python --version
```

Move to your specific directory and execute the program in the source directory. This will open up the program in your terminal to use basic ATM features as explained above.

```bash
python source/main.py
```

To run test cases, you can use the test file located in tests/test.py. This will automatically run unit-tests on the main functions within source/atm_controller.py.

```bash
python tests/test.py
```

**Note** that running the test file may generate terminal outputs that are unrelated to the tests. These are printed because I have included test cases for functions that generate some terminal outputs. Additionally, the program may pause for few seconds, and this is due to the sleep() function I have inserted for better user interface. However, these will not ultimately affect the test performance.
