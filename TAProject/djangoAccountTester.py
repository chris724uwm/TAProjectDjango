from django.test import TestCase
from TAProject.account import Account
from TAProject.models import AccountModel

class testDjangoAccount(TestCase):

    def setUp(self):
        self.superAccount = Account('SuperUser', 'SuperPass', 'SuperName', 'SuperAdd', 'SuperEmail', "1234567980", 0)
        self.TAAccount = Account('TAUser', 'TAPass', 'TAName', 'TAAdd', 'TAEmail', '1234567890', 3)

    def test_createAccount_exists(self):
        Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '1234567890', 0])
        checkAccount = AccountModel.objects.get(username='user', password='pass', name='name', address='address', email='email', phonenumber='1234567890', accountFlag=0)
        self.assertIsNotNone(checkAccount)

    def test_createAccount_short_list_length(self):
        self.assertEquals(self.superAccount.create_account(['user', 'pass', 'name', 'address']), "Account Creation Error: Wrong amount of information passed")

    def test_createAccount_long_list_length(self):
        self.assertEquals(self.superAccount.create_account(['user', 'pass', 'name', 'address', 'email', '2134235', 0, 'un-needed string']), "Account Creation Error: Wrong amount of information passed")

    def test_createAccount_wrong_permissions(self):
        self.assertEquals(self.TAAccount.create_account(['user', 'pass', 'name', 'address', 'email', '2134235', 0]), "Account Creation Error: You don't have permission")

    def test_createAccount_already_exists(self):
        self.superAccount.create_account(['user', 'pass', 'name', 'address', 'email', '1234567890', 0])
        self.assertEquals(self.superAccount.create_account(['user', 'pass', 'name', 'address', 'email', '1234567890', 0]),
                          "Account Creation Error: Username Already Exists")

    def test_deleteAccount_deletes(self):
        Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '1234567890', 0])
        Account.delete_account(self.superAccount, ['user'])
        self.assertTrue(not AccountModel.objects.filter(username='user'))

    def test_deleteAccount_wrong_permissions(self):
        self.assertEquals(self.TAAccount.delete_account(['user']), "Account Deletion Error: You don't have permission")

    def test_deleteAccount_does_not_exist(self):
        self.assertEquals(self.superAccount.delete_account(['userdoesnotexist']), "Account Deletion Error: No Such Account Exists")

    def test_deleteAccount_not_enough_perms(self):
        self.assertEquals(self.superAccount.delete_account([]),"Account Deletion Error: Wrong amount of information passed")

    def test_deleteAccount_username_not_str(self):
        self.assertEquals(self.superAccount.delete_account([1]), "Account Deletion Error: Incorrect username")
