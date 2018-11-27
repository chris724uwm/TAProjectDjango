from TAProject.models import AccountModel
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
        classlist.append(Course(classlist.__len__(), stringList[1]))
    def deleteClass(self, stringList):
        classlist.remove(classlist[int(stringList[1])])


    def assign_instructor_class(self, stringlist):
        #classlist[id].setInstructor(instructor)
        if self.accountFlag!=0:  #Check if supervisor is issuing command
            return "No Access to command"
        if AccountModel.objects.filter(name=stringlist[0]).exists():  #Check if account exists
            if CourseModel.objects.filter(id=int(stringlist[1])).exists():  #Check if course exists
                a = AccountModel.objects.get(name=stringlist[0])  #get account
                if a.accountFlag!=2:  #Make sure its instructor
                    return "Not Instructor"
                c = CourseModel.objects.get(id=int(stringlist[1]))  #Get course
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

    def unassign_instructor_class(self, id):
        classlist[id].setInstructor("No Instructor")

    def assign_TA_lab(self, stringlist):
        if self.accountFlag>3:  #Instructor above can only use this command
            return "No Access to command"
        if LabModel.objects.filter(id=int(stringlist[1])).exists():  #Make sure lab exists
            l = LabModel.objects.get(id=int(stringlist[1]))  #Get lab
            if AccountModel.objects.filter(name=stringlist[0]).exists():  #Make sure account exists
                a = AccountModel.objects.get(name=stringlist[0])  #Get account
                if a.accountFlag!=3:  #Make sure account is TA
                    return "You can only assign a TA to lab"
                l.ta = a
                l.save()
                return "TA Added to course" #Ta is added and saved
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
        if self.accountFlag != 0:
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
        if self.accountFlag != 0:
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
        return "account deleted"

    # edit methods work for both admin/supervisor edits and self edits
    # stringList[0] = username, stringList[1] = updated_name
    def edit_account_password(self, string_list):
        if self.username == string_list[0] or self.accountFlag == 0 or self.accountFlag == 1:
            if self.password == string_list[1]:
                print("it is the current password")
            elif string_list[1] is None:
                print("please enter something")
            else:
                self.password = string_list[1]
                print("password updated")
        else:
            print("You don't have permissions to edit this")

    # stringList[0] = username, stringList[1] = updated_name
    def edit_account_name(self, string_list):
        if self.username == string_list[0] or self.accountFlag == 0 or self.accountFlag == 1:
            if self.name == string_list[1]:
                print("it is the current name")
            elif string_list[1] is None:
                print("please enter something")
            else:
                self.name = string_list[1]
                print("name updated")
        else:
            print("You don't have permissions to edit this")

    # stringList[0] = username, stringList[1] = updated_address
    def edit_account_address(self, string_list):
        if self.username == string_list[0] or self.accountFlag == 0 or self.accountFlag == 1:
            if self.address == string_list[1]:
                print("it is the current address")
            elif string_list[1] is None:
                print("please enter something")
            else:
                self.address = string_list[1]
                print("address updated")
        else:
            print("You don't have permissions to edit this")

    # stringList[0] = username, stringList[1] = updated_email
    def edit_account_email(self, string_list):
        if self.username == string_list[0] or self.accountFlag == 0 or self.accountFlag == 1:
            if self.email == string_list[1]:
                print("it is the current email")
            elif string_list[1] is None:
                print("please enter something")
            else:
                self.email = string_list[1]
                print("email updated")
        else:
            print("You don't have permissions to edit this")

    # stringList[0] = username, stringList[1] = updated_phone_number
    def edit_account_phonenumber(self, string_list):
        if self.username == string_list[0] or self.accountFlag == 0 or self.accountFlag == 1:
            if self.phonenumber == string_list[1]:
                print("it is the current phone number")
            elif string_list[1] is None:
                print("please enter something")
            else:
                self.phonenumber = string_list[1]
                print("phone number updated")
        else:
            print("You don't have permissions to edit this")

myDict = {"createaccount": "createAccount","deleteaccount": "deleteAccount", "createclass": "createClass",
              "editaccount": "editaccounts(username)", "printallclass": "printAllClasses", "deleteclass": "deleteClass"}
