
class Course:

    def __init__(self,cCode, cName,inst =None,T = None):
        self.classCode = cCode
        self.className = cName
        self.instructor = inst
        self.TA = T

    def setClassCode(self, id):
        self.classCode = id

    def setClassName(self,name):
        self.className = name

    def setInstructor(self,instruct):
        self.instructor = instruct

    def setTA(self, T):
        self.TA = T

    def getClassCode(self):
        return(self.classCode)

    def getClassName(self):
        return(self.className)

    def getInstructor(self):
        if self.instructor is None:
            return ("There is no Instructor Assigned")
        else:
            return(self.instructor)

    def getTA(self):
        if self.TA is None:
            return ("There is no TA Assigned")
        else:
            return(self.TA)

    def printInfo(self):
        return "\nClass Code:" + str(self.getClassCode())\
               + "\nClass Name: " + self.getClassName() \
               + "\nProfessor: " + self.getInstructor()\
               +"\nTeachers Assistant: " + self.getTA()
