from django.test import TestCase
from TAProject.views import login,logout
from TAProject.models import AccountModel, LabModel, CourseModel


class TestLogin(TestCase):
    def setUp(self):
        logout(["logout"])
        AccountModel.objects.create(username="user123", password="pass321", name="guy", address="streetplace",
                                    email="email@yahoo.com", phonenumber="1235678", accountFlag=1)

    def test_login1(self):  # No username and password entered, no user logged in. Should return error
        self.assertEqual(login(["login"]), 'Error')

    def test_login2(self):  # only username, no user logged in. Should return error
        self.assertEqual(login(["login", "user123"]), "Error")

    def test_login3(self):  # only password, no user logged in. Should return error
        self.assertEqual(login(["login", "pass321"]), "Error")

    def test_wrong_pass(self):
        self.assertEqual(login(["login", "user123", "abcdefg"]), "Wrong Password")

    def test_login4(self):  # both, no user logged in. Should pass(Will fail until memory is complete)
        self.assertEqual(login(["login", "user123", "pass321"]), "Login Success")

    def test_login5(self):  # No username and password entered, user logged in. Should return error
        self.assertEqual(login(["login"]), "Error")

    def test_login6(self):  # only username, user logged in. Should return error
        self.assertEqual(login(["login", "user123"]), "Error")

    def test_login7(self):  # only password, user logged in. Should return error
        self.assertEqual(login(["login", "password"]), "Error")

    def test_login8(self):  # both, user logged in. Should return error
        self.assertEqual(login(["login", "user123", "pass321"]), "Login Success")
        self.assertEqual(login(["login", "user123", "pass321"]), "Another User is logged in")

    def test_login9(self):
        self.assertEqual(login(["login", "too", "many", "arguments"]), "Error")

    def test_logoff1(self):  # User logged in
        self.assertEqual(login(["login", "user123", "pass321"]), "Login Success")
        self.assertEqual(logout(["logout"]), "Logout Success")

    def test_logoff2(self):  # No one logged in
        self.assertEqual(logout(["logout"]), "Error")

    def test_logoff3(self):  # Someone passes extra arguments
        self.assertEqual(logout(["logout", "a", "b", "c"]), "Error")

    def test_loginLogoff(self):  # (Will fail until memory is complete)
        self.assertEqual(login(["login", "user123", "pass321"]), "Login Success")
        self.assertEqual(logout(["logout"]), "Logout Success")




#if __name__ == '__main__':
#    unittest.main()
