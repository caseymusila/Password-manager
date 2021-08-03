#!/usr/bin/env python3.9
from user import User

def create_account(username,password,account_type):
    new_user = User(username,password,account_type)
    return new_user

def save_account(user):
    user.save_user()

def del_account(user):
    user.delete_account()

def check_existing_accounts(username):
    return User.user_account_exists(username)

def display_accounts():
    return User.display_user()

def main():
    print("Welcome to your account manager.What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
               print("Use these codes : ca - create new account, da - display accounts, ex - exit")

               short_code = input().lower()

               if short_code == 'ca':
                   print("New Account")
                   print("-"*10)

                   print("Username...")
                   username =input()

                   print("Password...")
                   password = input()

                   print("Account type...")
                   account_type = input()


                   save_account(create_account(username,password,account_type))
                   print('\n')
                   print(f"New Account {username} created")
                   print('\n')

               elif short_code == 'da':

                   if display_accounts():
                       print("Here is a list of all your accounts ")
                       print('\n')

                       for user in display_accounts():
                           print(f"{user.username} {user.password}")

                           print('\n')
                   else:
                           print('\n')
                           print("You don't have any accounts yet")
                           print('\n')

               elif short_code == "ex":

                   print("Have a good day...")
                   break

               else:
                   print("Please use the short codes")


if __name__ == '__main__':

    main()


