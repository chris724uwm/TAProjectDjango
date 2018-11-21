from main import Project
import main
import unittest

console = Project()

class TestLogin(unittest.TestCase):
    def test_login1(self):  # No username and password entered, no user logged in. Should return error
        self.assertEqual(console.command("login"), "Error")

    def test_login2(self):  # only username, no user logged in. Should return error
        self.assertEqual(console.command("login username"), "Error")

    def test_login3(self):  # only password, no user logged in. Should return error
        self.assertEqual(console.command("login password"), "Error")

    def test_login4(self):  # both, no user logged in. Should pass(Will fail until memory is complete)
        self.assertEqual(console.command("login username password"), "Login Success")

    def test_login5(self):  # No username and password entered, user logged in. Should return error
        main.set_user(None)  # Just setting it to something for testing
        self.assertEqual(console.command("login"), "Error")

    def test_login6(self):  # only username, user logged in. Should return error
        self.assertEqual(console.command("login username"), "Error")

    def test_login7(self):  # only password, user logged in. Should return error
        self.assertEqual(console.command("login password"), "Error")

    def test_login8(self):  # both, user logged in. Should return error
        main.set_user(1)  # Just setting it to something for testing
        self.assertEqual(console.command("login username password"), "Another User is logged in")

    def test_login9(self):
        self.assertEqual(console.command("login too any arguements"), "Error")

    def test_logoff1(self):  # User logged in
        main.set_user(1)  # Just setting it to something for testing
        self.assertEqual(console.command("logout"), "Logout Success")

    def test_logoff2(self):  # No one logged in
        self.assertEqual(console.command("logout"), "Error")

    def test_logoff3(self):  # Someone passes extra arguements
        self.assertEqual(console.command("logout a b c"), "Error")

    def test_loginLogoff(self):  # (Will fail until memory is complete)
        main.set_user(None)  # Just setting it to something for testing
        self.assertEqual(console.command("login username password"), "Login Success")
        self.assertEqual(console.command("logout"), "Logout Success")


if __name__ == '__main__':
    unittest.main()
