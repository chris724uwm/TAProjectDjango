from TAProject.models import AccountModel, CourseModel, LabModel
from TAProject.Course import Course
classlist = []

#NOTES
#You may have to put these commands into the terminal if you get a no such table error
#
#python manage.py makemigrations
#
#python manage.py migrate --run-syncdb
#
#stack overflow link: https://stackoverflow.com/questions/12784835/django-no-such-table

class Account:

    def __init__(self, username, password, name, address, email, phonenumber, accountFlag):
        # for accountFlag: 0 is supervisor, 1 is administrator, 2 is instructor, 3 is TA
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.email = email
        self.phonenumber = phonenumber
        self.accountFlag = accountFlag

   
    def createClass(self, stringList):
        if CourseModel.objects.filter(number=stringList[0]).exists():
            return "Class Exists"
        newCourse = CourseModel(number=stringList[0], name=stringList[1])
        newCourse.save()
        return "Class Created"
    def createLab(self, stringList):
        course = CourseModel.objects.get(id = stringList[2])
        t = AccountModel.objects.get(username= stringList[1])
        newLab = LabModel(name = stringList[0], course = course, ta = t)
        newLab.save()
        return "Lab Created"

    def deleteClass(self, stringList):
        CourseModel.objects.filter(number=int(stringList[0])).delete()
        return "Course Deleted"

    def assign_instructor_class(self, stringlist):
        #classlist[id].setInstructor(instructor)
        if self.accountFlag!=0:  #Check if supervisor is issuing command
            return "No Access to command"
        if AccountModel.objects.filter(username=stringlist[0]).exists():  #Check if account exists
            if CourseModel.objects.filter(number=int(stringlist[1])).exists():  #Check if course exists
                a = AccountModel.objects.get(username=stringlist[0])  #get account
                if a.accountFlag!=2:  #Make sure its instructor
                    return "Not Instructor"
                c = CourseModel.objects.get(number=int(stringlist[1]))  #Get course
                if not c.instructor == None:  #Make sure course has no instructor
                    return "Course has instructor"
                else:
                    c.instructor=a
                    c.save()
                    return "Instructor Added to Course" #Set instructor as account and saves
            else:
                return "Course doesn't exist"
        else:
            return "Account Doesn't exist"

    def assign_TA_class(self, stringlist):
        if self.accountFlag!=0:  #Check if supervisor is issuing command
            return "No Access to command"
        if AccountModel.objects.filter(username=stringlist[1]).exists():  #Check if account exists
            if CourseModel.objects.filter(number=int(stringlist[0])).exists():  #Check if course exists
                a = AccountModel.objects.get(username=stringlist[1])  #get account
                if a.accountFlag!=3:  #Make sure its TA
                    return "Not TA"
                c = CourseModel.objects.get(number=int(stringlist[0]))  #Get course
                if not c.ta == None:  #Make sure course has no ta
                    return "Course has TA"
                else:
                    c.ta = a
                    c.save()
                    return "TA Added to Course" #Set instructor as account and saves
            else:
                return "Course doesn't exist"
        else:
            return "Account Doesn't exist"
        
    def unassign_instructor_class(self, id):
        classlist[id].setInstructor("No Instructor")

    def assign_TA_lab(self, stringlist):
        if self.accountFlag!=0 or self.accountFlag!=2:  #Instructor and super can only use this command
            return "No Access to command"
        if LabModel.objects.filter(id=int(stringlist[1])).exists():  #Make sure lab exists
            l = LabModel.objects.get(id=int(stringlist[1]))  #Get lab
            if AccountModel.objects.filter(username=stringlist[0]).exists():  #Make sure account exists
                a = AccountModel.objects.get(username=stringlist[0])  #Get account
                if a.accountFlag!=3:  #Make sure account is TA
                    return "You can only assign a TA to lab"
                l.ta = a
                l.save()
                return "TA Added to Lab" #Ta is added and saved
            else:
                return "TA does not exist"

        else:
            return "Lab doesn't exist"

    def unassign_TA_class(self, id):
        classlist[id].setTA["No TA"]

    def printAllClasses(self, stringlist):
        for x in range(0, len(classlist)):
            print(classlist[x].printInfo())

    def create_account(self, stringList):

        # must have the right amount of arguments
        if len(stringList) != 7:
            return "Account Creation Error: Wrong amount of information passed"

        # must have the right account permissions
        if self.accountFlag != 0 and self.accountFlag != 1:
            return "Account Creation Error: You don't have permission"

        # last variable in stringList should be a number between 0-3
        # convert accountFlag to int
        stringList[6] = (int)(stringList[6])
        if type(stringList[6]) is not int:
            return "Account Creation Error: Wrong account type"


        # account flag must be 0-3
        if stringList[6]<0 or stringList[6]>3:
            return "Account Creation Error: Invalid permissions given"

        # check if passed account flag is correct
        if stringList[6] is int and stringList[6]<0 or stringList[6]>3:
            return"Account Creation Error: Invalid account type"


        #check if username already exists
        checkAccount = AccountModel.objects.filter(username=stringList[0])

        if checkAccount:
            return "Account Creation Error: Username Already Exists"

        #create new AccountModel and save if username isnt taken
        newAccount = AccountModel(username=stringList[0], password=stringList[1],
                                  name=stringList[2], address=stringList[3],
                                  email=stringList[4], phonenumber=stringList[5], accountFlag=stringList[6])
        newAccount.save()
        # write it to memory
        #Memory.write_account(newAccount)
        return "Account Created"

    def delete_account(self, stringList):
        # must have the right amount of arguments
        if len(stringList) != 1:
            return "Account Deletion Error: Wrong amount of information passed"

        # must have the right account permissions
        if self.accountFlag != 0 and self.accountFlag != 1:
            return "Account Deletion Error: You don't have permission"

        # username must be a str
        if type(stringList[0]) is not str:
            return "Account Deletion Error: Incorrect username"

        #checks if account exists
        checkAccount = AccountModel.objects.filter(username=stringList[0])
        if not checkAccount:
            return "Account Deletion Error: No Such Account Exists"

        # deletes account from memory
        checkAccount.delete()
        return "Account Deleted"

    # edit methods work for both admin/supervisor edits and self edits
    # stringList[0] = username, stringList[1] = updated_name
    def edit_password(self, string_list):
        if len(string_list) != 2:
            return "Wrong number of arguments."
        if self.username == string_list[0]: #user is updating their own password
            if self.password == string_list[1]:
                return "Password entered is already " + string_list[0] + "'s current password."
            else:
                user = AccountModel.objects.get(username=string_list[0])
                user.password = string_list[1]
                user.save(update_fields=['password'])
                # self.password = string_list[1]
                # self.save(update_fields=['password'])
                return "Password updated."
        elif self.accountFlag == 0 or self.accountFlag == 1: #user is admin/supervisor and updating another user's password
            if AccountModel.objects.filter(username=string_list[0]).count() > 0:
                user = AccountModel.objects.get(username=string_list[0])
                if user.password == string_list[1]:
                    return "Password entered is already " + string_list[0] + "'s current password."
                else:
                    user.password = string_list[1]
                    user.save(update_fields=['password'])
                    return "Password updated."
            else:
                return "Error: username " + string_list[0] + " not found."
        else:
            return "You don't have permissions to edit this"

    # stringList[0] = username, stringList[1] = updated_name
    def edit_name(self, string_list):
        if len(string_list) != 2:
            return "Wrong number of arguments."
        if self.username == string_list[0]: #user is updating their own name
            if self.name == string_list[1]:
                return "Name entered is already " + string_list[0] + "'s current name."
            else:
                user = AccountModel.objects.get(username=string_list[0])
                user.name = string_list[1]
                user.save(update_fields=['name'])
                # self.name = string_list[1]
                # self.save(update_fields=['name'])
                return "Name updated."
        elif self.accountFlag == 0 or self.accountFlag == 1: #user is admin/supervisor and updating another user's name
            if AccountModel.objects.filter(username=string_list[0]).count() > 0:
                user = AccountModel.objects.get(username=string_list[0])
                if user.name == string_list[1]:
                    return "Name entered is already " + string_list[0] + "'s current name."
                else:
                    user.name = string_list[1]
                    user.save(update_fields=['name'])
                    return "Name updated."
            else:
                return "Error: username " + string_list[0] + " not found."
        else:
            return "You don't have permissions to edit this"

    # stringList[0] = username, stringList[1] = updated_address
    def edit_address(self, string_list):
        if len(string_list) != 2:
            return "Wrong number of arguments."
        if self.username == string_list[0]: #user is updating their own address
            if self.address == string_list[1]:
                return "Address entered is already " + string_list[0] + "'s current address."
            else:
                user = AccountModel.objects.get(username=string_list[0])
                user.address = string_list[1]
                user.save(update_fields=['address'])
                # self.address = string_list[1]
                # self.save(update_fields=['address'])
                return "Address updated."
        elif self.accountFlag == 0 or self.accountFlag == 1: #user is admin/supervisor and updating another user's address
            if AccountModel.objects.filter(username=string_list[0]).count() > 0:
                user = AccountModel.objects.get(username=string_list[0])
                if user.address == string_list[1]:
                    return "Address entered is already " + string_list[0] + "'s current address."
                else:
                    user.address = string_list[1]
                    user.save(update_fields=['address'])
                    return "Address updated."
            else:
                return "Error: username " + string_list[0] + " not found."
        else:
            return "You don't have permissions to edit this"

    # stringList[0] = username, stringList[1] = updated_email
    def edit_email(self, string_list):
        if len(string_list) != 2:
            return "Wrong number of arguments."
        if self.username == string_list[0]: #user is updating their own email
            if self.email == string_list[1]:
                return "Email entered is already " + string_list[0] + "'s current email."
            else:
                user = AccountModel.objects.get(username=string_list[0])
                user.email = string_list[1]
                user.save(update_fields=['email'])
                # self.email = string_list[1]
                # self.save(update_fields=['email'])
                return "Email updated."
        elif self.accountFlag == 0 or self.accountFlag == 1: #user is admin/supervisor and updating another user's email
            if AccountModel.objects.filter(username=string_list[0]).count() > 0:
                user = AccountModel.objects.get(username=string_list[0])
                if user.email == string_list[1]:
                    return "Email entered is already " + string_list[0] + "'s current email."
                else:
                    user.email = string_list[1]
                    user.save(update_fields=['email'])
                    return "Email updated."
            else:
                return "Error: username " + string_list[0] + " not found."
        else:
            return "You don't have permissions to edit this"

    # stringList[0] = username, stringList[1] = updated_phone_number
    def edit_phonenumber(self, string_list):
        if len(string_list) != 2:
            return "Wrong number of arguments."
        if self.username == string_list[0]: #user is updating their own phonenumber
            if self.phonenumber == string_list[1]:
                return "Phonenumber entered is already " + string_list[0] + "'s current phonenumber."
            else:
                user = AccountModel.objects.get(username=string_list[0])
                user.phonenumber = string_list[1]
                user.save(update_fields=['phonenumber'])
                # self.phonenumber = string_list[1]
                # self.save(update_fields=['phonenumber'])
                return "Phonenumber updated."
        elif self.accountFlag == 0 or self.accountFlag == 1: #user is admin/supervisor and updating another user's phonenumber
            if AccountModel.objects.filter(username=string_list[0]).count() > 0:
                user = AccountModel.objects.get(username=string_list[0])
                if user.phonenumber == string_list[1]:
                    return "Phonenumber entered is already " + string_list[0] + "'s current phonenumber."
                else:
                    user.phonenumber = string_list[1]
                    user.save(update_fields=['phonenumber'])
                    return "Phonenumber updated."
            else:
                return "Error: username " + string_list[0] + " not found."
        else:
            return "You don't have permissions to edit this"

    def view_my_TA(self):
        z=0
        if self.accountFlag == 2:
            for x in range(0, len(classlist)):
                if classlist[x].getInstructor == self.name:
                    z = 1
                    for e in AccountModel.objects.all():
                        if classlist[x].getTA == e.name:
                            tale = e.name, "|", e.email, "|", e.phonenumber
                            return tale
                        else:
                            return "you dont have any TA assigned yet"
            if z == 0:
                return "you dont have any course assigned to you yet"
        else:
            return "you are not allowed to view TAs' information"

    def view_all_accounts(self):
        if self.accountFlag == 0 or self.accountFlag == 1:
            all_info = ""
            for a in AccountModel.objects.all():
                all_info += "Username: " + a.username + ", password: " + a.password + ", name: " + a.name + ", address: " + a.address + ", email: " + a.email + ", phonenumber: " + a.phonenumber + ", account flag: " + str(a.accountFlag)
                all_info += '\n'
            return all_info
        else:
            return "You don't have permissions to view all information."

    def view_all_courses(self):
        if self.accountFlag == 0 or self.accountFlag == 1:
            all_info = ""
            for c in CourseModel.objects.all():
                all_info += "Course: " + c.name + " " + c.number

                all_info += '\n'
            return all_info
        else:
            return "You don't have permissions to view all information."

    def view_all_tas(self):
        if self.accountFlag == 0 or self.accountFlag == 1:
            all_info = ""
            for a in AccountModel.objects.filter(accountFlag=3):
                all_info += "Username: " + a.username + ", name: " + a.name
                all_info += '\n'
            return all_info
        else:
            return "You don't have permissions to view all information."

myDict = {"createaccount": "createAccount","deleteaccount": "deleteAccount", "createclass": "createClass",
              "editaccount": "editaccounts(username)", "printallclass": "printAllClasses", "deleteclass": "deleteClass"}
