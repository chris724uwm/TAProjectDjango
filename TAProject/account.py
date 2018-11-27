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

    def assign_instructor_class(self, instructor, id):
        classlist[id].setInstructor(instructor)

    def unassign_instructor_class(self, id):
        classlist[id].setInstructor("No Instructor")

    def assign_TA_class(self, T, id):
        classlist[id].setTA(T)

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
    def edit_password(self, string_list):
        if self.username == string_list[0]: #user is updating their own password
            if self.password == string_list[1]:
                return "Password entered is already " + string_list[0] + "'s current password."
            else:
                self.password = string_list[1]
                self.save(update_fields=['password'])
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
        if self.username == string_list[0]: #user is updating their own name
            if self.name == string_list[1]:
                return "Name entered is already " + string_list[0] + "'s current name."
            else:
                self.name = string_list[1]
                self.save(update_fields=['name'])
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
        if self.username == string_list[0]: #user is updating their own address
            if self.address == string_list[1]:
                return "Address entered is already " + string_list[0] + "'s current address."
            else:
                self.address = string_list[1]
                self.save(update_fields=['address'])
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
        if self.username == string_list[0]: #user is updating their own email
            if self.email == string_list[1]:
                return "Email entered is already " + string_list[0] + "'s current email."
            else:
                self.email = string_list[1]
                self.save(update_fields=['email'])
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
        if self.username == string_list[0]: #user is updating their own phonenumber
            if self.phonenumber == string_list[1]:
                return "Phonenumber entered is already " + string_list[0] + "'s current phonenumber."
            else:
                self.phonenumber = string_list[1]
                self.save(update_fields=['phonenumber'])
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

myDict = {"createaccount": "createAccount","deleteaccount": "deleteAccount", "createclass": "createClass",
              "editaccount": "editaccounts(username)", "printallclass": "printAllClasses", "deleteclass": "deleteClass"}
