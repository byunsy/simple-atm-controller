# simple-atm-controller

## Description

Simple-atm-controller allows users to interact with a terminal-based ATM machine. While the program does not integrate with a real bank system, it has basic and useful features like inserting a card, putting a corresponding PIN number, selecting an account (Checking and/or Savings), displaying the current balance, depositing, and withdrawing. A user can create an account with his or her choice of name, card number, and PIN number, all of which will be stored inside the program. Later on, as users insert their cards, their PIN numbers must match their card numbers they have specified when creating their accounts.

For simplicity, all account balances are represented as integers and every account user only have two accounts--checking and savings. Users are also unable to transfer money or withdraw more than their total balance. Moreover, since the users cannot actually 'insert' their cards, I have decided to simulate it instead by typing in their card numbers in the 'Insert Cards' action sequence.

## Basic Instructions

The program has four main steps.

1. Create Account

   - Before you insert your card, make sure that you have actually created an account using the ATM machine. Creating the account will require you to input your name, card number (XXXX-XXXX-XXXX-XXXX format), and PIN number (6 digits).
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

No additional installations are required for this repository, besides Python.

Make sure you are using Python 3 versions (I used Python 3.7.2).

## Usage

Firstly, clone the simple-atm-controller repository to your desired directory.

```bash
git clone https://github.com/byunsy/simple-atm-controller
```

Check and make sure you are using the correct version of Python.

```bash
python --version
```

In the directory you have cloned the repository, execute the program in the source directory. This will open up the program in your terminal to use basic ATM features as explained above.

```bash
python source/main.py
```

To run test cases, you can use the test file located in tests/test.py. This will automatically run unit tests on the main functions within source/atm_controller.py.

```bash
python tests/test.py
```

**Note** that running the test file may generate terminal outputs that are unrelated to the tests. These are printed because I have included test cases for functions that generate some terminal outputs. Additionally, the program may pause for few seconds, and this is due to the sleep() function I have inserted for better user interface purposes. However, these will not ultimately affect the test performance.
