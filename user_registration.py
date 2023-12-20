"""

@Author: Omkar Bhise

@Date: 2023-12-20 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-20 02:30:00

@Title :  User Registration Problem

"""
import re


class UserRegistration:

    def __init__(self, f_name):
        self.f_name = f_name

    def check_first_name(self):
        pattern = re.compile(r'^[A-Z][A-Za-z]{2,}$')
        if pattern.match(self.f_name):
            return True
        return False


if __name__ == '__main__':
    first_name = input("Enter the first name ")

    user = UserRegistration(first_name)

    if user.check_first_name():
        print("First name is valid ")
    else:
        print("First name is Not valid ")
