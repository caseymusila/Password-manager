import unittest


class User:
    account_list =[]

    def __init__(self,username,password,account_type):
        self.username = username
        self.password = password
        self.account_type = account_type

    def save_account(self):
        User.account_list.append(self)

    @classmethod
    def user_account_exists(cls,username):
        for user in cls.account_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_user(cls):
        return cls.account_list

    def delete_account(self):
        User.account_list.remove(self)
        

    

