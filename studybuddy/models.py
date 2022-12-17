from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

# from django.dispact import receiver
# Create your models here.



# class Profile(models.Model):

# Run python manage.py makemigrations studybuddy after changing this file
# Then run python manage.py migrate
class Department(models.Model):
    departmentAcronym = models.CharField(max_length=5)


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    member_list = models.ManyToManyField('UserT')
    study_sessions = models.ManyToManyField('Session')

    @admin.display(
        boolean=True,
    )
    def __str__(self):
        return self.group_name

class Session(models.Model):
    sessions = models.DateTimeField(default=now)
    @admin.display(
        boolean=True,
    )
    def __str__(self):
        return self.sessions

class Course(models.Model):
    course_IDI = models.CharField(max_length=150, default='NULL')
    course_sub = models.CharField(max_length = 300, default = 'NULL')
    course_log = {}
    groups_list = models.ManyToManyField(Group)

    @admin.display(
        boolean=True,
    )
    def __str__(self):
        return self.course_name


# @receiver(user_signed_up)
# @login_required
class UserT(models.Model):
    username = models.CharField(max_length=300)
    has_set_username = False
    email = models.CharField(max_length=500, default="NULL")
    GroupsList = models.ManyToManyField(Group)
    CourseList = models.ManyToManyField(Course)
    friends_list = models.ManyToManyField("UserT")


    @admin.display(
        boolean=True,
    )
    def __str__(self):
        return self.username