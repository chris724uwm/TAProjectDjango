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

def editPassword(args):
    if args[0] == "editPassword":
        if len(args) == 3:
            return account.edit_password(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editName(args):
    if args[0] == "editName":
        if len(args) == 3:
            return account.edit_name(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editAddress(args):
    if args[0] == "editAddress":
        if len(args) == 3:
            return account.edit_address(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editEmail(args):
    if args[0] == "editEmail":
        if len(args) == 3:
            return account.edit_email(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editPhonenumber(args):
    if args[0] == "editPhonenumber":
        if len(args) == 3:
            return account.edit_phonenumber(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def viewAccount(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
  if args[0] == "addUser":
    return "I am addUser"
  else:
     return ""

# <<<Add your commands to commandList>>>
commandList = [createAccount, deleteAccount,
               editAddress, editEmail,
               editName, editPassword,
               editPhonenumber, viewAccount]

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
