"""============================================================================
TITLE      : test.py
AUTHOR     : Sang Yoon Byun
DESCRIPTION: A simple unit test that checks the important functions inside
             source/atm_controller.py.
============================================================================"""

import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.append(parent_dir) 

import unittest
from unittest.mock import patch

from source import atm_controller as ac


"""----------------------------------------------------------------------------
TestAccountClass
  - This will check if classes are constructed correctly and whether 
    class variables and methods are working properly.
----------------------------------------------------------------------------"""
class TestAccountClass(unittest.TestCase):

    def test_class_vars(self):
        person = ac.Account('Sang Yoon Byun', '1111-2222-3333-4444', '123456')

        self.assertEqual(person.get_name(), 'Sang Yoon Byun')
        self.assertEqual(person.get_card_num(), '1111-2222-3333-4444')
        self.assertEqual(person.get_pin_num(), '123456')

    def test_class_methods(self):
        person = ac.Account('Sang Yoon Byun', '1111-2222-3333-4444', '123456')

        # Test checking account methods
        person.c_deposit('1000')
        self.assertEqual(person.c_get_balance(), 1000)

        person.c_withdraw('1000')
        self.assertEqual(person.c_get_balance(), 0)

        person.c_withdraw('1')
        self.assertEqual(person.c_get_balance(), 0)

        # Test savings account methods
        person.s_withdraw('500')
        self.assertEqual(person.s_get_balance(), 0)

        person.s_deposit('500')
        self.assertEqual(person.s_get_balance(), 500)

        person.s_deposit('500')
        self.assertEqual(person.s_get_balance(), 1000)


"""----------------------------------------------------------------------------
TestInputChecks
  - This will check if the two important checking systems (check_card_num and 
    check_pin_num) are effectively checking user inputs.
----------------------------------------------------------------------------"""
class TestInputChecks(unittest.TestCase):

    def test_check_card_num(self):
        # Test whether check_card_num works properly
        self.assertFalse(ac.check_card_num("1234123412341234"))
        self.assertFalse(ac.check_card_num("1234_1234_1234_1234"))
        self.assertFalse(ac.check_card_num("1234.1234.1234.1234"))

        self.assertFalse(ac.check_card_num("1234-1234-1234-123"))
        self.assertFalse(ac.check_card_num("1234-1234-123-41234"))
        self.assertFalse(ac.check_card_num("1234-1234-1234-123a"))

        self.assertFalse(ac.check_card_num("aaaa-aaaa-aaaa-aaaa"))
        self.assertFalse(ac.check_card_num("    -    -    -    "))
        self.assertFalse(ac.check_card_num(""))

        self.assertTrue(ac.check_card_num("1234-1234-1234-1234"))
        self.assertTrue(ac.check_card_num("0000-0000-0000-0000"))

    def test_check_pin_num(self):
        # Test whether check_card_num works properly
        self.assertFalse(ac.check_pin_num("abcdef"))
        self.assertFalse(ac.check_pin_num("12345"))
        self.assertFalse(ac.check_pin_num("12345a"))

        self.assertFalse(ac.check_pin_num("123aaa"))
        self.assertFalse(ac.check_pin_num("aaaaaa"))
        self.assertFalse(ac.check_pin_num("......"))

        self.assertFalse(ac.check_pin_num("12345 "))
        self.assertFalse(ac.check_pin_num("      "))
        self.assertFalse(ac.check_pin_num(""))

        self.assertTrue(ac.check_pin_num("123456"))


"""----------------------------------------------------------------------------
TestCardPIN
  - This will check if the function is able to accurately match the card number
    and PIN number as stored in the system (accounts_list). 
----------------------------------------------------------------------------"""
class TestCardPIN(unittest.TestCase):

    # We can use patch from unittest.mock to test inputs.

    def test_verification_1(self):
        # 1. Create an account and append it to the list
        person = ac.Account('Harry Potter', '1111-2222-3333-4444', '123456')
        ac.accounts_list.append(person)

        user_input_1 = ['1111-2222-3333-4444', '123456']

        with patch('builtins.input', side_effect=user_input_1):
            self.assertEqual(ac.verification(), (True, 0))
    
    def test_verification_2(self):
        # 2. Create an account and append it to the list
        person = ac.Account('Ron Weasley', '9999-8888-7777-6666', '111999')
        ac.accounts_list.append(person)

        user_input_2 = ['9999-8888-7777-6666', '111999']

        with patch('builtins.input', side_effect=user_input_2):
            self.assertEqual(ac.verification(), (True, 1))

        ##### card number should not be found #####
        user_input_3 = ['9999-8888-7777-5555', '111999']

        with patch('builtins.input', side_effect=user_input_3):
            self.assertEqual(ac.verification(), (False, None))

    def test_verification_3(self):
        # 3. Create an account and append it to the list
        person = ac.Account('Hermione Granger', '1234-1234-1234-1234', '987654')
        ac.accounts_list.append(person)

        user_input_4 = ['1234-1234-1234-1234', '987654']

        with patch('builtins.input', side_effect=user_input_4):
            self.assertEqual(ac.verification(), (True, 2))

        user_input_5 = ['1234-1234-1234-1234', '999999']

        ##### PIN number should not match with card number #####
        with patch('builtins.input', side_effect=user_input_5):
            self.assertEqual(ac.verification(), (False, None))


if __name__ == '__main__':
    unittest.main()