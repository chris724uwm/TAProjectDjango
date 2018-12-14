from django.shortcuts import render
from django.views import View
from TAProject.models import AccountModel, CourseModel, LabModel
from TAProject.account import Account
from django.views.generic.edit import CreateView
from TAProject.forms import CreateAccountForm,DeleteAccountForm,CreateCourseForm, DeleteCourseForm, AssignTACourseForm, viewTAAssignmentForm, AssignInstructorCourseForm, loginForm


#variable for current account
#when starting makes a default supervisor account
global account
account = Account('superUser','superPassword', 'superName','superAddress', 'superEmail', '1234567890', 0)
superuser = AccountModel(username=account.username,
                         password=account.password,name=account.name,address=account.address,
                         email=account.email,phonenumber=account.phonenumber,accountFlag=account.accountFlag)
#superuser.save()

def getuser():  # Get current user
    return account

def setuser(user):
    global account
    account = user

def help(args):
    #command list
    if args[0] == "help":
        return "1.createAccount\n2.deleteAccount\n3.editPassword\n" \
               "4.editName\n5.editAddress\n6.editEmail\n" \
               "7.editPhonenumber\n8.viewAccount\n9.createCourse\n" \
               "10.createLab\n11.printAllLab\n12.deleteCourse\n" \
               "13.printAllCourse\n14.assignInstructorClass\n15.assignTALab\n" \
               "16.AssignTACourse\n17.login\n18.logout\n" \
               "19.viewMyTA\n20.viewAll\n"
    else:
        return ""

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
    if account is None:  # make sure an account is logged in
      return "Nobody Logged in"
    if len(args) == 2:
        return account.delete_account(args[1:2])
    else:
        return "wrong amount of arguments"
  else:
      return ""

def editPassword(args):
    if args[0] == "editPassword":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        if len(args) == 3:
            return account.edit_password(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editName(args):
    if args[0] == "editName":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        if len(args) == 3:
            return account.edit_name(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editAddress(args):
    if args[0] == "editAddress":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        if len(args) == 3:
            return account.edit_address(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editEmail(args):
    if args[0] == "editEmail":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        if len(args) == 3:
            return account.edit_email(args[1:3])
        else:
            return "Wrong number of arguments."
    else:
        return ''

def editPhonenumber(args):
    if args[0] == "editPhonenumber":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
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
def createCourse(args):
  #if args[0] == addUser, adds user named args[1]
  #returns "User <args[1]> added" or "User <args[1]> exists"
  #else returns ""
    if account is None:  # make sure an account is logged in
      return "Nobody Logged in"
    if args[0] == "createCourse":
        return account.createClass(args)
    else:
        return ""
def createLab(args):
    if account is None:  # make sure an account is logged in
        return "Nobody Logged in"
    if args[0] == "createLab":
        return account.createLab(args)
    else:
        return ""
def printAllLab(args):
    if args[0] == "printAllLab":
        return LabModel.objects.all().values()
    else:
        return ""

def viewMyLab(args):

    t = AccountModel.objects.get(username = args[0])
    return LabModel.objects.filter(ta = t)

def deleteCourse(args):
    if account is None:  # make sure an account is logged in
        return "Nobody Logged in"
    if args[0]== "deleteCourse":
        return account.deleteClass(args)
    else:
        return""
def printAllCourses(args):
    # if args[0] == addUser, adds user named args[1]
    # returns "User <args[1]> added" or "User <args[1]> exists"
    # else returns ""
    if args[0] == "printAllCourses":
        return CourseModel.objects.all().values()
    else:
        return ''
def assignInstructorClass(args):
    #If args[0] == assigninstructorclass, adds Instructor to course.
    if args[0] == "assignInstructorClass":
        if account is None: #make sure account exists
            return "Nobody Logged in"
        if len(args)==3: #right number of arguements
            return account.assign_instructor_class(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""

def assignTALab(args):
    if args[0] == "assignTALab": #make sure this command is being called
        if account is None:  #make sure an account is logged in
            return "Nobody Logged in"
        if len(args)==3:  #make sure right number of arguments
            return account.assign_TA_lab(args[1:])
        else:
            return "Wrong number of arguments"
    else:
        return ""

def assignTACourse(args):
    if args[0] == "assignTACourse": #make sure this command is being called
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

def viewMyTA(args):
    if args[0] == "viewMyTA":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        return account.view_my_TA()
    else:
        return ""

def viewAll(args):
    if args[0] == "viewAll":
        if account is None:  # make sure an account is logged in
            return "Nobody Logged in"
        return account.view_all()
    else:
        return ""

# <<<Add your commands to commandList>>>
commandList = [createAccount, deleteAccount,
               editAddress, editEmail,
               editName, editPassword,
               editPhonenumber, viewAccount, assignInstructorClass, assignTALab, assignTACourse,login, logout,viewMyTA,
               viewAll, createLab, printAllLab,createCourse, deleteCourse,
               assignInstructorClass, assignTALab, assignTACourse,printAllCourses]

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
    form = loginForm()
    return render(request, "main/index.html", {'form': form})

  def post(self,request):
    form = loginForm()
    #out = doStuff(request.POST["command"],commandList)
    user = request.POST["username"]
    passw = request.POST["password"]
    if AccountModel.objects.filter(username=user).exists():
        a = AccountModel.objects.get(username=user)
        if a.password == passw:
            request.session["user"] = user
            request.session["flag"] = a.accountFlag
            return sendToPage(a.accountFlag, request)
            #if a.accountFlag == 0:
            #   return render(request, "main/supervisor_home_page.html")
            #elif a.accountFlag == 1:
            #    return render(request, "main/admin_home_page.html")
            #elif a.accountFlag == 2:
            #    return render(request, "main/instructor_home_page.html")
            #else:
            #    return render(request, "main/ta_home_page.html")
        else:
            return render(request, "main/index.html", {'form': form})

    else:
        return render(request, "main/index.html", {'form': form})

pagelist = []


def toSuper(arg, request):
    if arg == 0:
        return render(request, "main/supervisor_home_page.html")
    else:
        return ""


pagelist.append(toSuper)


def toAdmin(arg, request):
    if arg == 1:
        return render(request, "main/admin_home_page.html")
    else:
        return ""

pagelist.append(toAdmin)

def toInstructor(arg, request):
    if arg == 2:
        return render(request, "main/instructor_home_page.html")
    else:
        return ""

pagelist.append(toInstructor)


def toTA(arg, request):
    if arg == 3:
        return render(request, "main/ta_home_page.html")
    else:
        return ""


pagelist.append(toTA)


def sendToPage(arg, request):
    for i in pagelist:
        x = i(arg, request)
        if not x == "":
            return x

class Supervisor(View):
    def get(self,request):
        return render(request, "main/supervisor_home_page.html")
class Admin(View):
    def get(self,request):
        return render(request, "main/admin_home_page.html")
class Instructor(View):
    def get(self,request):
        return render(request, "main/instructor_home_page.html")
class TA(View):
    def get(self,request):
        return render(request, "main/ta_home_page.html")

class CreateAccount(View):

#    def get(self,request):
#       return render(request, "main/create_account.html")

    def get(self, request):
        #creates new instance of CreateAccountForm
        form = CreateAccountForm()
        # gives this form to the webpage
        user = request.session['user']
        flag = request.session['flag']
        return render(request, "main/create_account.html", {'form': form, 'accountFlag' :flag, 'flag':flag ,'user' :user,'username':user})

    def post(self,request):
        form = CreateAccountForm(request.POST)

        #checks if form is valid then saves all the entered data
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            accountFlag = form.cleaned_data['accountFlag']

        #get current user, gets response from create_account
        currentUser = AccountModel.objects.get(username=request.session['user'])
        currentUser = Account(currentUser.username, currentUser.password, currentUser.name, currentUser.address,
                              currentUser.email, currentUser.phonenumber, currentUser.accountFlag)
        submitMessage = currentUser.create_account([username,password,name,address, email, phonenumber, accountFlag])
        #creats list to send back to page
        flag = request.session['flag']
        user = request.session['user']
        args = {'form': form, 'submitMessage':submitMessage, 'accountFlag': flag, 'flag': flag, 'user': user, 'username': user}
        return render(request, "main/create_account.html", args)

class DeleteAccount(View):

    def get(self,request):
        #creates new form
        form = DeleteAccountForm()
        #returns form and accountFlag to page
        user = request.session['user']
        flag = request.session['flag']
        return render(request, "main/create_account.html",
                      {'form': form, 'accountFlag': flag, 'flag': flag, 'user': user, 'username': user})

    def post(self,request):
        form = DeleteAccountForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

        #gets current user and send info to delete_account and saves response
        currentUser = AccountModel.objects.get(username=request.session['user'])
        currentUser = Account(currentUser.username, currentUser.password ,currentUser.name ,currentUser.address ,currentUser.email ,currentUser.phonenumber ,currentUser.accountFlag)
        submitMessage = currentUser.delete_account([username])
        #returns form and submitmessage
        flag = request.session['flag']
        user = request.session['user']
        args = {'form': form, 'submitMessage': submitMessage, 'accountFlag': flag, 'flag': flag, 'user': user, 'username': user}
        return render(request, "main/delete_account.html", args)

class CreateCourse(View):

    def get(self, request):
        #creates new instance of CreateAccountForm
        form = CreateCourseForm()
        # gives this form to the webpage
        return render(request, "main/create_course.html", {'form': form, 'accountFlag' :account.accountFlag})

    def post(self,request):
        form = CreateCourseForm(request.POST)
        #checks if form is valid then saves all the entered data
        if form.is_valid():
            number = form.cleaned_data['number']
            name = form.cleaned_data['name']

        #gets response from create_account
        submitMessage = account.createClass([number, name])
        #creats list to send back to page
        args = {'form': form, 'submitMessage':submitMessage, 'accountFlag': account.accountFlag}
        return render(request, "main/create_course.html", args)
class DeleteCourse(View):

    def get(self,request):
        #creates new form
        form = DeleteCourseForm()
        #returns form and accountFlag to page
        return render(request, "main/delete_course.html", {'form':form, 'accountFlag':account.accountFlag})

    def post(self,request):
        form = DeleteCourseForm(request.POST)

        if form.is_valid():
            id = form.cleaned_data['id']

        #send info to delete_account and saves response
        submitMessage = account.deleteClass([id])
        #returns form and submitmessage
        args = {'form': form, 'submitMessage': submitMessage, 'accountFlag': account.accountFlag}
        return render(request, "main/delete_course.html", args)
class AssignTACourse(View):

    def get(self,request):
        #creates new form
        form = AssignTACourseForm()
        #returns form and accountFlag to page
        return render(request, "main/assign_ta_course.html", {'form':form, 'accountFlag':account.accountFlag})

    def post(self,request):
        form = AssignTACourseForm(request.POST)

        if form.is_valid():
            courseNum = form.cleaned_data['Course']
            taUserName = form.cleaned_data['Username']

        #send info to delete_account and saves response
        submitMessage = account.assign_TA_class([courseNum,taUserName])
        #returns form and submitmessage
        args = {'form': form, 'submitMessage': submitMessage, 'accountFlag': account.accountFlag}
        return render(request, "main/assign_ta_course.html", args)
class viewTAAssignment(View):

    def get(self,request):
        #creates new form
        form = viewTAAssignmentForm()
        #returns form and accountFlag to page
        return render(request, "main/view_ta_assignments.html", {'form':form, 'accountFlag':account.accountFlag})

    def post(self,request):
        form = viewTAAssignmentForm(request.POST)

        if form.is_valid():
            Username = form.cleaned_data['Username']

        #send info to delete_account and saves response
        submitMessage = viewMyLab([Username])
        #returns form and submitmessage
        args = {'form': form, 'submitMessage': submitMessage, 'accountFlag': account.accountFlag}
        return render(request, "main/view_ta_assignments.html", args)
class AssignInstructorCourse(View):

    def get(self,request):
        #creates new form
        form = AssignInstructorCourseForm()
        #returns form and accountFlag to page
        return render(request, "main/assign_instructor_course.html", {'form':form, 'accountFlag':account.accountFlag})

    def post(self,request):
        form = AssignInstructorCourseForm(request.POST)

        if form.is_valid():
            Username = form.cleaned_data['Username']
            id = form.cleaned_data['id']

        #send info to delete_account and saves response
        submitMessage = account.assign_instructor_class([Username, id])
        #returns form and submitmessage
        args = {'form': form, 'submitMessage': submitMessage, 'accountFlag': account.accountFlag}
        return render(request, "main/assign_instructor_course.html", args)