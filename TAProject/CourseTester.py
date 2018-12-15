from TAProject.Course import Course
import unittest

a = Course(0,"Class Name","professor","TA")
class TestCourseMethods(unittest.TestCase):
    def setUp(self):
       a = Course(0,"Class Name","professor","TA")

    def test_getClassCode(self):
        self.assertEqual(a.getClassCode(), 0)

    def test_getClassName(self):
        self.assertEqual(a.getClassName(), "Class Name")

    def test_getInstructor(self):
        self.assertEqual(a.getInstructor(), "professor")

    def test_getTA(self):
        self.assertEqual(a.getTA(), "TA")

    def test_setClassCode(self):
        self.assertEqual(a.getClassCode(), 0)

    def test_setClassName(self):
        a.setClassName("ClassName")
        self.assertEqual(a.className, "ClassName")

    def test_setInstructor(self):
        a.setInstructor("prof")
        self.assertEqual(a.instructor, "prof")

    def test_setTA(self):
        a.setTA("T")
        self.assertEqual(a.TA, "T")

if __name__ == '__main__':
    unittest.main()
