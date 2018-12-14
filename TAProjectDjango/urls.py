"""TAProjectDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import TAProject
from TAProject.views import Home
from TAProject.views import Supervisor
from TAProject.views import Admin
from TAProject.views import Instructor
from TAProject.views import TA
from TAProject.views import CreateAccount, DeleteAccount, CreateCourse, DeleteCourse, AssignTACourse, viewTAAssignment, AssignInstructorCourse
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', Home.as_view()),
    path('supervisor_home_page.html', Supervisor.as_view()),
    path('admin_home_page.html', Admin.as_view()),
    path('instructor_home_page.html', Instructor.as_view()),
    path('ta_home_page.html', TA.as_view()),
    path('create_account.html', CreateAccount.as_view()),
    path('delete_account.html', DeleteAccount.as_view()),
    path('create_course.html', CreateCourse.as_view()),
    path('delete_course.html', DeleteCourse.as_view()),
    path('assign_ta_course.html', AssignTACourse.as_view()),
    path('view_ta_assignments.html', viewTAAssignment.as_view()),
    path('assign_instructor_course.html', AssignInstructorCourse.as_view()),

]
