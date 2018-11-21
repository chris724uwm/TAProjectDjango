from account import Account
import unittest

user = Account('Snowman', '20181225', 'SnowJackal', 'backyard',
               'merryXmas@winter.com', 414000111, 3)  # does flag number matters here?
class TestAccountMethods(unittest.TestCase):

    def setUp(self):
        self.superAccount = Account('SuperUser', 'SuperPass', 'SuperName', 'SuperAdd', 'SuperEmail', "1234567980", 0)
        self.TAAccount = Account('TAUser', 'TAPass', 'TAName', 'TAAdd', 'TAEmail', '1234567890', 3)
        self.admin_test = Account('admin', 'password', 'first last', '123 main st', 'admin@aol.com', '4141234567', 0);

    def test_createAccount_short_list_length(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address'])

    def test_createAccount_long_list_length(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 0, 'un-needed string'])

    def test_createAccount_wrong_permissions(self):
        with self.assertRaises(Exception):
            Account.create_account(self.TAAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 0])

    def test_createAccount_wrong_permissions_passed(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 'not an int'])

    def test_createAccount_permission_passed_too_low(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', -1])

    def test_createAccount_permission_passed_too_high(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 4])

    def test_deleteAccount_wrong_permissions(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.TAAccount, ['username'])

    def test_deleteAccount_incorrect_username(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [9])

    def test_deleteAccount_short_list(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [])

    def test_deleteAccount_long_list(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [0, 1, 2])

    def test_password1(self):
        self.assertEqual(user.edit_account_password("20181225"), "it is the current password")

    def test_password2(self):
        self.assertEqual(user.edit_account_password("20181231"), "password updated")

    def test_password3(self):
        self.assertEqual(user.edit_account_password(), "plz enter something")

    def test_name1(self):
        self.assertEqual(user.edit_account_name("SnowJackal"), "it is the current name")

    def test_name2(self):
        self.assertEqual(user.edit_account_name("FireFly"), "name updated")

    def test_name3(self):
        self.assertEqual(user.edit_account_name(), "plz enter something")

    def test_address1(self):
        self.assertEqual(user.edit_account_address("backyard"), "it is the current address")

    def test_address2(self):
        self.assertEqual(user.edit_account_address("street"), "address updated")

    def test_address3(self):
        self.assertEqual(user.edit_account_address(), "plz enter something")

    def test_email1(self):
        self.assertEqual(user.edit_account_email("merryXmas@winter.com"), "it is the current email")

    def test_email2(self):
        self.assertEqual(user.edit_account_email("seeyounextyear@spring.com"), "email updated")

    def test_email3(self):
        self.assertEqual(user.edit_account_email(), "plz enter something")

    def test_phonenumber1(self):
        self.assertEqual(user.edit_account_phonenumber(414000111), "it is the current phonenumber")

    def test_phonenumber2(self):
        self.assertEqual(user.edit_account_phonenumber(414222333), "phonenumber updated")

    def test_phonenumber3(self):
        self.assertEqual(user.edit_account_phonenumber(), "plz enter something")


if __name__ == '__main__':
    unittest.main()
