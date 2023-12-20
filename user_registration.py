"""

@Author: Omkar Bhise

@Date: 2023-12-20 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-20 02:30:00

@Title :  User Registration Problem

"""
import re


class UserRegistration:

    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def check_first_name(self):
        pattern = re.compile(r'^[A-Z][A-Za-z]{2,}$')
        if pattern.match(self.f_name):
            return True
        return False

    def check_last_name(self):  # ^ string start with
        pattern = re.compile(r'^[A-Z][A-Za-z]{2,}$')  # $ end of the string
        if pattern.match(self.l_name):
            return True
        return False

    def check_email(self):
        pattern = re.compile(r'^[a-z]+\.?[a-z0-9]*?@[a-z]+\.[a-z0-9]+\.?[a-z]+?$')
        #                       abc     .xyz        @   bl  .co     .in

        if pattern.match(self.email):
            return True
        return False


if __name__ == '__main__':
    first_name = input("Enter the first name ")
    last_name = input("Enter the last name ")
    email = input("Enter the email ")

    user = UserRegistration(first_name, last_name, email)

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

