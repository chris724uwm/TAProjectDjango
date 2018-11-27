from django.shortcuts import render
from django.views import View
from TAProject.account import Account

#variable for current account
#when starting makes a default supervisor account
account = Account('superUser','superPassword', 'superName',
                   'superAddress', 'superEmail', '1234567890', 0)

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
        if len(args)==3:
            return account.assign_instructor_class(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""

def assignTALab(args):
    if args[0] == "assigntalab":
        if len(args)==3:
            return account.assign_TA_lab(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""


# <<<Add your commands to commandList>>>
commandList = [createAccount, deleteAccount,
               editAccountAddress, editAccountEmail,
               editAccountName, editAccountPassword,
               editAccountPhonenumber, viewAccount, assignInstructorClass, assignTALab]

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
