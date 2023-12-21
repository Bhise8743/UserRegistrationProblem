"""

@Author: Omkar Bhise

@Date: 2023-12-20 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-20 02:30:00

@Title :  User Registration Problem

"""
import re


class UserRegistration:

    def __init__(self, f_name, l_name, email, m_num, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.m_num = m_num
        self.password = password

    def check_first_name(self):
        """
        Description: This function validate first name.

        Parameter: self object as parameter.

        Return: boolean value

        """
        pattern = re.compile(r'^[A-Z][A-Za-z]{2,}$')
        if pattern.match(self.f_name):
            return True
        return False

    def check_last_name(self):  # ^ string start with
        """
        Description: This function validate last name.

        Parameter: self object as parameter.

        Return: boolean value

        """
        pattern = re.compile(r'^[A-Z][A-Za-z]{2,}$')  # $ end of the string
        if pattern.match(self.l_name):
            return True
        return False

    def check_email(self):
        """
        Description: This function validate email.

        Parameter: self object as parameter.

        Return: boolean value

        """
        pattern = re.compile(r'^[a-z]+\.?[a-z0-9]*?@[a-z]+\.[a-z0-9]+\.?[a-z]+?$')
        #                       abc     .xyz        @   bl  .co     .in

        if pattern.match(self.email):
            return True
        return False

    def check_mobile_num(self):
        """
        Description: This function validate mobile number.

        Parameter: self object as parameter.

        Return: boolean value

        """
        pattern = re.compile(r'\d\d [6-9]\d{9}')
        if pattern.match(self.m_num):
            return True
        return False

    def check_password(self):
        """
        Description: This function validate password.

        Parameter: self object as parameter.

        Return: boolean value

        """
        # pattern = re.compile(r'\D{8,}')  # \D  - Not a Digit (0-9)
        # pattern = re.compile(r'(?=.*[A-Z]){8,}')   # .* it check the in all character of the password
        # pattern = re.compile(r'(?=.*[A-Z])(?=.*[0-9]){8,}')
        pattern = re.compile(r'(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*+/-]){8,}')
        if pattern.match(self.password):
            return True
        return False


if __name__ == '__main__':
    first_name = input("Enter the first name ")
    last_name = input("Enter the last name ")
    email = input("Enter the email ")
    m_num = input("Enter the Mobile number ")
    password = input("Enter the password ")

    user = UserRegistration(first_name, last_name, email, m_num, password)

    if user.check_first_name():
        print("First name is valid ")
    else:
        print("First name is Not valid ")

    if user.check_last_name():
        print("Last name is valid ")
    else:
        print("Last name is Not valid ")

    if user.check_email():
        print("Email is valid ")
    else:
        print("Email is Not valid")

    if user.check_mobile_num():
        print("Mobile number is valid ")
    else:
        print("Mobile number is Not valid ")

    if user.check_password():
        print("Password is valid ")
    else:
        print("Password is Not valid ")
