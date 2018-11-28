from django.test import TestCase
from TAProject.account import Account
from TAProject.models import AccountModel

class testDjangoAccount(TestCase):

    def setUp(self):
        self.superAccount = Account('SuperUser', 'SuperPass', 'SuperName', 'SuperAdd', 'SuperEmail', "1234567980", 0)
        self.TAAccount = Account('TAUser', 'TAPass', 'TAName', 'TAAdd', 'TAEmail', '1234567890', 3)
        self.supervisor = Account('supervisor', 'supervisor_password', 'supervisor_name', 'supervisor_address', 'supervisor_email', "414", 0)
        self.admin = Account('admin', 'admin_password', 'admin_name', 'admin_address', 'admin_email', "262", 0)
        self.instructor = Account('instructor', 'instructor_password', 'instructor_name', 'instructor_address', 'instructor_email', "920", 0)
        self.ta = Account('ta', 'ta_password', 'ta_name', 'ta_address', 'ta_email', "715", 0)

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


    def test_edit_password_wrong_number_arguments(self):
        self.assertEqual(self.supervisor.edit_password(["supervisor", "password_update", "extra_arg1"]), "Wrong number of arguments.")
        self.assertEqual(self.admin.edit_password(["admin"]), "Wrong number of arguments.")
        self.assertEqual(self.instructor.edit_password(["instructor", "password_update", "extra_arg1", "extra_arg2"]), "Wrong number of arguments.")
        self.assertEqual(self.ta.edit_password(["ta", "password_update", "extra_arg"]), "Wrong number of arguments.")

    def test_edit_password_self_same_password(self):
        self.assertEqual(self.supervisor.edit_password(["supervisor", "supervisor_password"]), "Password entered is already supervisor's current password.")
        self.assertEqual(self.admin.edit_password(["admin", "admin_password"]), "Password entered is already admin's current password.")
        self.assertEqual(self.instructor.edit_password(["instructor", "instructor_password"]), "Password entered is already instructor's current password.")
        self.assertEqual(self.ta.edit_password(["ta", "ta_password"]), "Password entered is already ta's current password.")

    def test_edit_password_self_updated(self):
        self.assertEqual(self.supervisor.edit_password(["supervisor", "supervisor_wordpass"]), "Password updated.")
        self.assertEqual(self.supervisor.password, "supervisor_wordpass")
        self.assertEqual(self.admin.edit_password(["admin", "admin_wordpass"]), "Password updated.")
        self.assertEqual(self.admin.password, "admin_wordpass")
        self.assertEqual(self.instructor.edit_password(["instructor", "instructor_wordpass"]), "Password updated.")
        self.assertEqual(self.instructor.password, "instructor_wordpass")
        self.assertEqual(self.ta.edit_password(["ta", "ta_wordpass"]), "Password updated.")
        self.assertEqual(self.ta.password, "ta_wordpass")

    def test_edit_password_wrong_permissions(self):
        self.assertEqual(self.instructor.edit_password(["supervisor", "password"]), "You don't have permissions to edit this")
        self.assertEqual(self.ta.edit_password(["admin", "password"]), "You don't have permissions to edit this")

    def test_edit_password_same_password(self):
        self.assertEqual(self.supervisor.edit_password(["instructor", "instructor_password"]), "Password entered is already instructor's current password.")
        self.assertEqual(self.admin.edit_password(["ta", "ta_password"]), "Password entered is already ta's current password.")

    def test_edit_password_updated(self):
        self.assertEqual(self.supervisor.edit_password(["instructor", "instructor_wordpass"]), "Password updated.")
        self.assertEqual(self.instructor.password, "instructor_wordpass")
        self.assertEqual(self.admin.edit_password(["ta", "ta_wordpass"]), "Password updated.")
        self.assertEqual(self.ta.password, "ta_wordpass")

    def test_edit_password_user_not_found(self):
        self.assertEqual(self.supervisor.edit_password(["unknown_user", "password"]), "Error: username unknown_user not found.")
        self.assertEqual(self.admin.edit_password(["user_not_found", "password"]), "Error: username user_not_found not found.")

    def test_edit_name_wrong_number_arguments(self):
        self.assertEqual(self.supervisor.edit_name(["supervisor", "name_update", "extra_arg1"]), "Wrong number of arguments.")
        self.assertEqual(self.admin.edit_name(["admin"]), "Wrong number of arguments.")
        self.assertEqual(self.instructor.edit_name(["instructor", "name_update", "extra_arg1", "extra_arg2"]), "Wrong number of arguments.")
        self.assertEqual(self.ta.edit_name(["ta", "name_update", "extra_arg"]), "Wrong number of arguments.")

    def test_edit_name_self_same_name(self):
        self.assertEqual(self.supervisor.edit_name(["supervisor", "supervisor_name"]), "Name entered is already supervisor's current name.")
        self.assertEqual(self.admin.edit_name(["admin", "admin_name"]), "Name entered is already admin's current name.")
        self.assertEqual(self.instructor.edit_name(["instructor", "instructor_name"]), "Name entered is already instructor's current name.")
        self.assertEqual(self.ta.edit_name(["ta", "ta_name"]), "Name entered is already ta's current name.")

    def test_edit_name_self_updated(self):
        self.assertEqual(self.supervisor.edit_name(["supervisor", "supervisor_name_new"]), "Name updated.")
        self.assertEqual(self.supervisor.name, "supervisor_name_new")
        self.assertEqual(self.admin.edit_name(["admin", "admin_name_new"]), "Name updated.")
        self.assertEqual(self.admin.name, "admin_name_new")
        self.assertEqual(self.instructor.edit_name(["instructor", "instructor_name_new"]), "Name updated.")
        self.assertEqual(self.instructor.name, "instructor_name_new")
        self.assertEqual(self.ta.edit_name(["ta", "ta_name_new"]), "Name updated.")
        self.assertEqual(self.ta.name, "ta_name_new")

    def test_edit_name_wrong_permissions(self):
        self.assertEqual(self.instructor.edit_name(["supervisor", "name"]), "You don't have permissions to edit this")
        self.assertEqual(self.ta.edit_name(["admin", "name"]), "You don't have permissions to edit this")

    def test_edit_name_same_name(self):
        self.assertEqual(self.supervisor.edit_name(["instructor", "instructor_name"]), "Name entered is already instructor's current name.")
        self.assertEqual(self.admin.edit_name(["ta", "ta_name"]), "Name entered is already ta's current name.")

    def test_edit_name_updated(self):
        self.assertEqual(self.supervisor.edit_name(["instructor", "instructor_name_up"]), "Name updated.")
        self.assertEqual(self.instructor.name, "instructor_name_up")
        self.assertEqual(self.admin.edit_name(["ta", "ta_name_up"]), "Name updated.")
        self.assertEqual(self.ta.name, "ta_name_up")

    def test_edit_name_user_not_found(self):
        self.assertEqual(self.supervisor.edit_name(["unknown_user", "name"]), "Error: username unknown_user not found.")
        self.assertEqual(self.admin.edit_name(["user_not_found", "name"]), "Error: username user_not_found not found.")

    def test_edit_address_wrong_number_arguments(self):
        self.assertEqual(self.supervisor.edit_address(["supervisor", "address_update", "extra_arg1"]), "Wrong number of arguments.")
        self.assertEqual(self.admin.edit_address(["admin"]), "Wrong number of arguments.")
        self.assertEqual(self.instructor.edit_address(["instructor", "address_update", "extra_arg1", "extra_arg2"]), "Wrong number of arguments.")
        self.assertEqual(self.ta.edit_address(["ta", "address_update", "extra_arg"]), "Wrong number of arguments.")

    def test_edit_address_self_same_address(self):
        self.assertEqual(self.supervisor.edit_address(["supervisor", "supervisor_address"]), "Address entered is already supervisor's current address.")
        self.assertEqual(self.admin.edit_address(["admin", "admin_address"]), "Address entered is already admin's current address.")
        self.assertEqual(self.instructor.edit_address(["instructor", "instructor_address"]), "Address entered is already instructor's current address.")
        self.assertEqual(self.ta.edit_address(["ta", "ta_address"]), "Address entered is already ta's current address.")

    def test_edit_address_self_updated(self):
        self.assertEqual(self.supervisor.edit_address(["supervisor", "supervisor_address_up"]), "Address updated.")
        self.assertEqual(self.supervisor.address, "supervisor_address_up")
        self.assertEqual(self.admin.edit_address(["admin", "admin_address_up"]), "Address updated.")
        self.assertEqual(self.admin.address, "admin_address_up")
        self.assertEqual(self.instructor.edit_address(["instructor", "instructor_address_up"]), "Address updated.")
        self.assertEqual(self.instructor.address, "instructor_address_up")
        self.assertEqual(self.ta.edit_address(["ta", "ta_address_up"]), "Address updated.")
        self.assertEqual(self.ta.address, "ta_address_up")

    def test_edit_address_wrong_permissions(self):
        self.assertEqual(self.instructor.edit_address(["supervisor", "address"]), "You don't have permissions to edit this")
        self.assertEqual(self.ta.edit_address(["admin", "address"]), "You don't have permissions to edit this")

    def test_edit_address_same_address(self):
        self.assertEqual(self.supervisor.edit_address(["instructor", "instructor_address"]), "Address entered is already instructor's current address.")
        self.assertEqual(self.admin.edit_address(["ta", "ta_address"]), "Address entered is already ta's current address.")

    def test_edit_address_updated(self):
        self.assertEqual(self.supervisor.edit_address(["instructor", "address_new"]), "Address updated.")
        self.assertEqual(self.instructor.address, "address_new")
        self.assertEqual(self.admin.edit_address(["ta", "address_new_ta"]), "Address updated.")
        self.assertEqual(self.ta.address, "address_new_ta")

    def test_edit_address_user_not_found(self):
        self.assertEqual(self.supervisor.edit_address(["unknown_user", "address"]), "Error: username unknown_user not found.")
        self.assertEqual(self.admin.edit_address(["user_not_found", "address"]), "Error: username user_not_found not found.")

    def test_edit_email_wrong_number_arguments(self):
        self.assertEqual(self.supervisor.edit_email(["supervisor", "email_update", "extra_arg1"]), "Wrong number of arguments.")
        self.assertEqual(self.admin.edit_email(["admin"]), "Wrong number of arguments.")
        self.assertEqual(self.instructor.edit_email(["instructor", "email_update", "extra_arg1", "extra_arg2"]), "Wrong number of arguments.")
        self.assertEqual(self.ta.edit_email(["ta", "email_update", "extra_arg"]), "Wrong number of arguments.")

    def test_edit_email_self_same_email(self):
        self.assertEqual(self.supervisor.edit_email(["supervisor", "supervisor_email"]), "Email entered is already supervisor's current email.")
        self.assertEqual(self.admin.edit_email(["admin", "admin_email"]), "Email entered is already admin's current email.")
        self.assertEqual(self.instructor.edit_email(["instructor", "instructor_email"]), "Email entered is already instructor's current email.")
        self.assertEqual(self.ta.edit_email(["ta", "ta_email"]), "Email entered is already ta's current email.")

    def test_edit_email_self_updated(self):
        self.assertEqual(self.supervisor.edit_email(["supervisor", "new1"]), "Email updated.")
        self.assertEqual(self.supervisor.email, "new1")
        self.assertEqual(self.admin.edit_email(["admin", "new2"]), "Email updated.")
        self.assertEqual(self.admin.email, "new2")
        self.assertEqual(self.instructor.edit_email(["instructor", "new3"]), "Email updated.")
        self.assertEqual(self.instructor.email, "new3")
        self.assertEqual(self.ta.edit_email(["ta", "new4"]), "Email updated.")
        self.assertEqual(self.ta.email, "new4")

    def test_edit_email_wrong_permissions(self):
        self.assertEqual(self.instructor.edit_email(["supervisor", "email"]), "You don't have permissions to edit this")
        self.assertEqual(self.ta.edit_email(["admin", "email"]), "You don't have permissions to edit this")

    def test_edit_email_same_email(self):
        self.assertEqual(self.supervisor.edit_email(["instructor", "instructor_email"]), "Email entered is already instructor's current email.")
        self.assertEqual(self.admin.edit_email(["ta", "ta_email"]), "Email entered is already ta's current email.")

    def test_edit_email_updated(self):
        self.assertEqual(self.supervisor.edit_email(["instructor", "new_email"]), "Email updated.")
        self.assertEqual(self.instructor.email, "new_email")
        self.assertEqual(self.admin.edit_email(["ta", "email_new"]), "Email updated.")
        self.assertEqual(self.ta.email, "email_new")

    def test_edit_email_user_not_found(self):
        self.assertEqual(self.supervisor.edit_email(["unknown_user", "email"]), "Error: username unknown_user not found.")
        self.assertEqual(self.admin.edit_email(["user_not_found", "email"]), "Error: username user_not_found not found.")

    def test_edit_phonenumber_wrong_number_arguments(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["supervisor", "phonenumber_update", "extra_arg1"]), "Wrong number of arguments.")
        self.assertEqual(self.admin.edit_phonenumber(["admin"]), "Wrong number of arguments.")
        self.assertEqual(self.instructor.edit_phonenumber(["instructor", "phonenumber_update", "extra_arg1", "extra_arg2"]), "Wrong number of arguments.")
        self.assertEqual(self.ta.edit_phonenumber(["ta", "phonenumber_update", "extra_arg"]), "Wrong number of arguments.")

    def test_edit_phonenumber_self_same_phonenumber(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["supervisor", "414"]), "Phonenumber entered is already supervisor's current phonenumber.")
        self.assertEqual(self.admin.edit_phonenumber(["admin", "262"]), "Phonenumber entered is already admin's current phonenumber.")
        self.assertEqual(self.instructor.edit_phonenumber(["instructor", "920"]), "Phonenumber entered is already instructor's current phonenumber.")
        self.assertEqual(self.ta.edit_phonenumber(["ta", "715"]), "Phonenumber entered is already ta's current phonenumber.")

    def test_edit_phonenumber_self_updated(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["supervisor", "111"]), "Phonenumber updated.")
        self.assertEqual(self.supervisor.phonenumber, "111")
        self.assertEqual(self.admin.edit_phonenumber(["admin", "222"]), "Phonenumber updated.")
        self.assertEqual(self.admin.phonenumber, "222")
        self.assertEqual(self.instructor.edit_phonenumber(["instructor", "333"]), "Phonenumber updated.")
        self.assertEqual(self.instructor.phonenumber, "333")
        self.assertEqual(self.ta.edit_phonenumber(["ta", "444"]), "Phonenumber updated.")
        self.assertEqual(self.ta.phonenumber, "444")

    def test_edit_phonenumber_wrong_permissions(self):
        self.assertEqual(self.instructor.edit_phonenumber(["supervisor", "phonenumber"]), "You don't have permissions to edit this")
        self.assertEqual(self.ta.edit_phonenumber(["admin", "phonenumber"]), "You don't have permissions to edit this")

    def test_edit_phonenumber_same_phonenumber(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["instructor", "920"]), "Phonenumber entered is already instructor's current phonenumber.")
        self.assertEqual(self.admin.edit_phonenumber(["ta", "715"]), "Phonenumber entered is already ta's current phonenumber.")

    def test_edit_phonenumber_updated(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["instructor", "555"]), "Phonenumber updated.")
        self.assertEqual(self.instructor.phonenumber, "555")
        self.assertEqual(self.admin.edit_phonenumber(["ta", "666"]), "Phonenumber updated.")
        self.assertEqual(self.ta.phonenumber, "666")

    def test_edit_phonenumber_user_not_found(self):
        self.assertEqual(self.supervisor.edit_phonenumber(["unknown_user", "phonenumber"]), "Error: username unknown_user not found.")
        self.assertEqual(self.admin.edit_phonenumber(["user_not_found", "phonenumber"]), "Error: username user_not_found not found.")