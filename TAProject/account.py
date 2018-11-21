from memory import Memory
from Course import Course
classlist = []
class Account:

    def __init__(self, username, password, name, address, email, phonenumber, accountFlag):
        # for accountFlag: 0 is supervisor, 1 is administrator, 2 is instructor, 3 is TA
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.email = email
        self. phonenumber = phonenumber
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
        if stringList.amount() != 7:
            raise Exception("Account Creation Error: Wrong amount of information passed")
            return

        # must have the right account permissions
        if self.accountFlag != 0:
            raise Exception("Account Creation Error: You don't have permission")
            return

        # last variable in stringList should be a number between 0-3
        if stringList[7] is not int:
            raise Exception("Account Creation Error: Wrong account type")
            return

        # account flag must be 0-3
        if stringList[7]<0 or stringList>3:
            raise Exception("Account Creation Error: Invalid permissions given")
            return

        # check if passed account flag is correct
        if stringList[7] is int and stringList[7]<0 or stringList[7]>3:
            raise Exception("Account Creation Error: Invalid account type")
            return

        # call constructor with correct information
        newAccount = Account(stringList[0], stringList[1], stringList[2], stringList[3], stringList[4], stringList[5], stringList[6])

        # write it to memory
        Memory.write_account(newAccount)
        return

    def delete_account(self, stringList):
        # must have the right amount of arguments
        if stringList.amount() != 1:
            raise Exception("Account Deletion Error: Wrong amount of information passed")
            return

        # must have the right account permissions
        if self.accountFlag != 0:
            raise Exception("Account Deletion Error: You don't have permission")
            return

        # username must be a str
        if stringList[0] is not str:
            raise Exception("Account Deletion Error: Incorrect username")
            return

        # deletes account from memory
        Memory.delete_account(stringList[0])
        return

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

myDict = {"createaccount": "createAccount","deleteaccount": "deleteAccount", "createclass": createClass,
              "editaccount": "editaccounts(username)", "printallclass": printAllClasses, "deleteclass": deleteClass}
