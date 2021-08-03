import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
      self.new_login = User("caseymusila","casey","github") 

    def test_init(self):
      self.assertEqual(self.new_login.username,"caseymusila")
      self.assertEqual(self.new_login.password,"casey")
      self.assertEqual(self.new_login.account_type,"github")
    
    def test_save_account(self):
        self.new_login.save_account()
        self.assertEqual(len(User.account_list), 1)
    
    def tearDown(self):
        User.account_list = []

    def test_user_account_exists(self):
        self.new_login.save_account()
        test_user = User("username","password","account_type")
        test_user.save_account()
        user_account_exists =User.user_account_exists("username")
        self.assertTrue(user_account_exists)

    def test_display_user_accounts(self):
        self.assertEqual(User.display_user(),User.account_list)

    def test_delete_account(self):
        self.new_login.save_account()
        test_user = User("username","password","account_type")
        test_user.save_account()

        self.new_login.delete_account()
        self.assertEqual(len(User.account_list),1)
        
if __name__ == '__main__':
    unittest.main()