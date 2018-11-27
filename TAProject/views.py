from django.shortcuts import render
from django.views import View
from TAProject.models import AccountModel, CourseModel, LabModel
from TAProject.account import Account

#variable for current account
#when starting makes a default supervisor account
global account
account = Account('superUser','superPassword', 'superName','superAddress', 'superEmail', '1234567890', 0)

def getuser():  # Get current user
    return account

def setuser(user):
    global account
    account = user

def createAccount(args):
  #if there are 8 things in args[] calls create_account in Account class
  #else prints 'wrong amount of arguments'
  if args[0] == 'createAccount':
      if len(args) == 8:
          return account.create_account(args[1:8])
      else:
          return "wrong amount of arguments"
  else:
      return ''

def deleteAccount(args):
  #if args[0] == deleteAccount,
  #calls delete_account if there are 2 args

  if args[0] == "deleteAccount":
    if len(args) == 2:
        return account.delete_account(args[1:2])
    else:
        return "wrong amount of arguments"
  else:
      return ""

def editAccountPassword(args):

  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def editAccountName(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def editAccountAddress(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def editAccountEmail(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def editAccountPhonenumber(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def viewAccount(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

def assignInstructorClass(args):
    #If args[0] == assigninstructorclass, adds Instructor to course.
    if args[0] == "assigninstructorclass":
        if account is None: #make sure account exists
            return "Nobody Logged in"
        if len(args)==3: #right number of arguements
            return account.assign_instructor_class(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""

def assignTALab(args):
    if args[0] == "assigntalab": #make sure this command is being called
        if account is None:  #make sure an account is logged in
            return "Nobody Logged in"
        if len(args)==3:  #make sure right number of arguments
            return account.assign_TA_lab(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""

def assignTACourse(args):
    if args[0] == "assigntaclass": #make sure this command is being called
        if account is None:  #make sure an account is logged in
            return "Nobody Logged in"
        if len(args)==3:  #make sure right number of arguments
            return account.assign_TA_class(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""


def login(args):
    if args[0] == "login":  #this command is called
        if len(args) != 3:  #Right amount of args
            return "Error"
        elif not account is None:  # no one else is logged in
            return "Another User is logged in"
        else:
            if AccountModel.objects.filter(username=args[1]).exists():  # check is account with that user exists
                a = AccountModel.objects.get(username=args[1])  #check is passwords match
                if not a.password == args[2]:  #passwords dont match
                    return "Wrong Password"
                user = Account(a.username, a.password, a.name, a.address, a.email, a.phonenumber, a.accountFlag) #setaccount
                setuser(user)
                return "Login Success"
            else:
               return "No such Username"
    else:
        return""

def logout(args):  # Log Off Command, extra is unnecessary arguments passed through
    user = getuser()
    if args[0] == "logout":
        if len(args) > 1:  # If any extra arguments
            return "Error"
        if user is None:  # We can't logoff if there is nobody to logoff
            return "Error"
        else:  # Set current user to none since no one is logged in
            setuser(None)
            return "Logout Success"
    else:
        return ""

# <<<Add your commands to commandList>>>
commandList = [createAccount, deleteAccount,
               editAccountAddress, editAccountEmail,
               editAccountName, editAccountPassword,
               editAccountPhonenumber, viewAccount, assignInstructorClass, assignTALab, assignTACourse,login, logout]

def doStuff(s, commandList):
  args = s.split(" ")
  for i in commandList:
    out = i(args)
    if out != "": #if i matches arg[0], stop looping
      break
  if out == "":
    out = "command not found"
  return out

# Create your views here.

class Home(View):
  def get(self,request):
    return render(request,"main/index.html")
  def post(self,request):
    out = doStuff(request.POST["command"],commandList)
    return render(request,"main/index.html", {"out":out})
