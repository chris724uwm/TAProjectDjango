from django.test import TestCase
from TAProject.views import assignInstructorClass, assignTACourse, assignTALab, login, logout
from TAProject.models import AccountModel, LabModel, CourseModel

# Create your tests here.


class AccountTests(TestCase):
    def setUp(self):
        AccountModel.objects.create(username="sup123", password="pass321", name="supervisor", address="streetplace100",
                                    email="email@yahoo.com", phonenumber="1235678", accountFlag=0)
        AccountModel.objects.create(username="ad123", password="pass321", name="admin", address="streetplace1",
                                    email="email@yahoo.com", phonenumber="1235678", accountFlag=1)
        AccountModel.objects.create(username="in123", password="pass321", name="instructor", address="streetplace2",
                                    email="email@yahoo.com", phonenumber="1235678", accountFlag=2)

        AccountModel.objects.create(username="ta123", password="pass321", name="ta", address="streetplace3",
                                    email="email@yahoo.com", phonenumber="1235678", accountFlag=3)

        CourseModel.objects.create(number="100", name="Engineering")

        LabModel.objects.create(name="Lab101")
        course = CourseModel.objects.get(number="100")
        lab = LabModel.objects.get(name="Lab101")
        lab.course = course

        logout(["logout"])
        login(["login","sup123", "pass321"])

    def testAssignInstructorCourse1(self):  # Instructor doesn't exist
        self.assertEqual(assignInstructorClass(["assignInstructorClass", "somedude", "100"]), "Account Doesn't exist")

    def testAssignInstructorCourse2(self):  # Course doesn't exist
        self.assertEqual(assignInstructorClass(["assignInstructorClass", "in123", "1014123"]), "Course doesn't exist")

    def testAssignInstructorCourse3(self):  # Wrong number of arguments
        self.assertEqual(assignInstructorClass(["assignInstructorClass"]), "Wrong number of arguments")

    def testAssignInstructorCourse4(self):  # Try to Add wrong account flag
        self.assertEqual(assignInstructorClass(["assignInstructorClass", "ta123", "100"]), "Not an Instructor")

    def testAssignInstructorCourse5(self):  # Correct Use
        self.assertEqual(assignInstructorClass(["assignInstructorClass", "in123", "100"]), "Instructor Added")

    def testAssignTACourse1(self):  # Instructor doesn't exist
        self.assertEqual(assignTACourse(["assigntaclass", "somedude", "100"]), "Account Doesn't exist")

    def testAssignTACourse2(self):  # Course doesn't exist
        self.assertEqual(assignTACourse(["assigntaclass", "in123", "1014123"]), "Course doesn't exist")

    def testAssignTACourse3(self):  # Wrong number of arguments
        self.assertEqual(assignTACourse(["assigntaclass"]), "Wrong number of arguments")

    def testAssignTACourse4(self):  # Try to Add wrong account flag
        self.assertEqual(assignTACourse(["assigntaclass", "in123", "100"]), "Not TA")

    def testAssignTACourse5(self):  # Correct Use
        self.assertEqual(assignTACourse(["assigntaclass", "ta123", "100"]), "TA Added")

    def testAssignTALab1(self):  # Instructor doesn't exist
        self.assertEqual(assignTALab(["assigntalab", "somedude", "Lab101"]), "Account Doesn't exist")

    def testAssignTALab2(self):  # Course doesn't exist
        self.assertEqual(assignTALab(["assigntalab", "in123", "lab123123"]), "Lab doesn't exist")

    def testAssignTALab3(self):  # Wrong number of arguments
        self.assertEqual(assignTALab(["assigntalab"]), "Wrong number of arguments")

    def testAssignTALab4(self):  # Try to Add wrong account flag
        self.assertEqual(assignTALab(["assigntalab", "in123", "Lab101"]), "Not TA")

    def testAssignTALab5(self):  # Supervisor can't add TA to lab only instructor
        self.assertEqual(assignTALab(["assigntalab", "ta123", "Lab101"]), "No Access to this comaamand")

    def testAssignTaLab6(self):  # Correct Use
        logout(["logout"])
        login(["login", "in123", "pass321"])
        self.assertEqual(assignTALab(["assigntalab", "ta123", "Lab101"]), "TA Added")
