#!/bin/env python3

import datetime as dt

# Parcent Class Users
class User:
    def __init__(self, name, birthdate, gender):
        self.name = name
        self.birthDate  = birthdate
        self.gender = gender

    def show_detail(self):
        print('Personal Details')
        print('')
        print('Name: ', self.name)
        print('Age', self.birthDate)
        print('Gender', self.gender)

# Child Class, Class inheritance
class Bank(User):
    def __init__(self, name, birth, gender):
        super().__init__(name, birth, gender)
        self.balance = 0

    # Deposit function
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('Account balance:', self.balance, 'THB')

    # Withdrawal function
    def withdraw(self, amount):
        self.amount = amount
        if self.balance > self.amount:
            self.balance = self.balance - self.amount ## Balance take away
            print('Account balance:', self.balance, 'THB')
        else:
            print('Insufficient fund!! | Your balance available: ', self.balance, 'THB')
    
    def view_balance(self):
        self.show_detail()
        print('Account balance:', self.balance, 'THB')

if __name__ == "__main__":    
    acc = Bank('Joe', '03/10/1993', 'Male')
    acc.deposit(100)
    acc.deposit(200)
    acc.deposit(300)
    acc.withdraw(200)
    acc.view_balance()
