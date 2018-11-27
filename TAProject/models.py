from django.db import models

class AccountModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=10)
    accountFlag = models.IntegerField()

class CourseModel(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    instructor = models.ForeignKey(AccountModel, on_delete=models.CASCADE, null=True, related_name='instructor')
    ta = models.ForeignKey(AccountModel, on_delete=models.CASCADE, null=True, related_name='ta')

Class LabModel(models.Model):
    name = models.CharField(max_length=20)
    ta = models.ForeignKey(AccountModel, on_delete=models.CASCADE, null=True, blank= True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, blank = True)
