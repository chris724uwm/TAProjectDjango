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

