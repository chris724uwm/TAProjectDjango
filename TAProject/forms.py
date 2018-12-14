from django import forms

#sets up fields for forms

class CreateAccountForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    phonenumber = forms.CharField(max_length=10)
    accountFlag = forms.IntegerField()

class DeleteAccountForm(forms.Form):
    username = forms.CharField(max_length=20)
class CreateCourseForm(forms.Form):
    number = forms.IntegerField()
    name = forms.CharField(max_length=20)
class DeleteCourseForm(forms.Form):
    id = forms.IntegerField()
class AssignTACourseForm(forms.Form):
    Course = forms.IntegerField()
    Username = forms.CharField(max_length=20)
class viewTAAssignmentForm(forms.Form):
    Username = forms.CharField(max_length=20)
class AssignInstructorCourseForm(forms.Form):
    Username = forms.CharField(max_length=20)
    id = forms.IntegerField()