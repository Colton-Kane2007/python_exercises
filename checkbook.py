# IGNORE (imported for testing)
# import os to use os.path.exists
# import os
# from checkbook_functions import current_balance
# from checkbook_functions import askwithdraw
# from checkbook_functions import money
# from checkbook_functions import putaway
# from checkbook_functions import askdeposit
# all my functions
# put all functions in checkbook_functions

# i need a file for my changing balance to live so it is still there after i exit
balance_lives_here = 'blh.txt'

import os

# building "view current balance"
# balance needs to be in a file so it exists after exiting
def current_balance():
    # need to start balance at 0
    balance = 0
    # need to access the file my balance lives in
    if os.path.exists('blh.txt'):
        with open('blh.txt', 'r') as f:
            # f.read? or variable in f?
            for var in f:
                # need thing that holds deposit and withdraw, split to make each a list
                give_take, amount = var.split(",")
                # need amount for how much to give or take from balance as an integer
                amount = int(amount)
                # have to add amount to balance 
                if give_take == "deposit":
                    balance += amount
                # subtract amount
                elif give_take == "withdraw":
                    balance -= amount
    print(f"Your current balance is ${balance}")

# building "record a debit (withdraw)"
# i need to take input(money) out of balance
# ask amount
# use input as a float, connect it to a function to ask amount
def askwithdraw():
    # money gives prompt
    amount = money()
    putaway("withdraw", amount)

# need a way to get an amount to use
# make sure it is a number
# always give an answer instead of just breaking
def money():
    amount = input("Enter the amount: ")
    if amount.isdigit():
        return amount
    else:
        print("Invalid input. Please enter a valid amount")

# need a function to put away changes made by deposit and withdraw into file for later use
# take in give_take and amount 
def putaway(give_take, amount):
    if os.path.exists('blh.txt'):
        with open('blh.txt', 'a') as file:
            # file.write to be able to edit balance
            file.write(f"{give_take}, {amount}")

# building "record a credit (deposit)"
# need to add input(money) to balance
# use input as a float to add to balance
# rinse and repeat askwithdraw
def askdeposit():
    amount = money()
    putaway("deposit", amount)

# building home page
def home():
    while True:
        print(' ')
        print('~~~ Welcome to your terminal checkbook! ~~~')
        print(' ')
        print('What would you like to do?')
        print('1) view current balance')
        print('2) record a debit (withdraw)')
        print('3) record a credit (deposit)')
        print('4) exit')
        print(' ')
        choice = input('Please enter a number 1, 2, 3, or 4: ')
        print("Your choice?", choice)
        if not choice.isdigit():
            print("Invalid input. Please enter a number 1, 2, 3, or 4")
            continue
        if choice == '1':
            current_balance()
            continue
        elif choice == '2':
            askwithdraw()
            continue
        elif choice == '3':
            askdeposit()
            continue
        elif choice == '4':
            print("Thanks, have a great day!")
            exit()
        else:
            print("Invalid input. Please enter a number 1, 2, 3, or 4")
            continue


if __name__ == "__main__":
    home()

