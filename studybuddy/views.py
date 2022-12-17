
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from .models import Group, Course, UserT, Session
import requests
import json
from django.urls import reverse
# from .forms import NameForm
from .models import Department
from studybuddy.forms import StudySessionForm
from django.http import HttpResponse, HttpResponseRedirect
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
import urllib


def studybuddy(request):
    return render(request, 'studybuddy.html', {})


def getDepartments(request, ind):
    # info = urllib.request.urlopen('http://luthers-list.herokuapp.com/api/deptlist/?format=json', data=None)
    # departments = info.read()
    # dept = eval(departments)
    # dept[ind].save()

    # return render(request, 'departments.html', {})
    response = requests.get(' http://luthers-list.herokuapp.com/api/deptlist').json()
    return render(request, 'departments.html', {'response': response})


def getAllDepartments(request):
    # info = urllib.request.urlopen('http://luthers-list.herokuapp.com/api/deptlist/?format=json', data=None)
    # departments = info.read()
    # dept = eval(departments)
    # for i in range(len(dept)):
    #    dept[i].save()

    # return render(request, 'departments.html', {})
    response = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
    # print(response)
    # print(response[0]['subject'])
    # list of department
    # per department, a list of all courses
    course_list = {}
    course_list2 = []
    response2 = response[0]['subject']
    base_url = "http://luthers-list.herokuapp.com/api/dept/"
    formatting = "?format=json"
    temp_list = []
    for i in range(len(response)):
        response2 = requests.get(base_url + response[i]['subject'] + formatting).json()
        for l in range(len(response2)):
            if response2[l]['description'] not in temp_list:
                temp_list.append(response2[l]['description'])
                course_list2.append(response2[l])
        course_list[response[i]['subject']] = course_list2
        course_list2 = []

    return render(request, 'departments.html', {'response': response, 'response2': course_list})


def getClassesFromDepartment(request, givenDepartment):
    # formattedString = 'http://luthers-list.herokuapp.com/api/dept/' + givenDepartment + '?format=json'
    # info = urllib.request.urlopen(formattedString, data=None)
    # classes = info.read()
    # cla = eval(classes)
    # for i in range(len(cla)):
    #   cla[i].save()

    # return render(request, 'classes.html', {})
    response = requests.get(' http://luthers-list.herokuapp.com/api/deptlist').json()
    return render(request, 'departments.html', {'response': response})


class GroupView(generic.ListView):
    model = Group
    template_name = 'groups/GroupsView.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        return Group.objects.all()


class GroupViewForm(generic.CreateView):
    model = Group
    template_name = 'groups/GroupsForm.html'
    fields = ['group_name', 'course_name']
    context_object_name = 'groups_list'
    success_url = 'view/'

    def get_queryset(self):
        return Group.objects.user_set()

def StudySessionView(request, group_ID):
    group = Group.objects.get(id=group_ID)
    studysessionform = StudySessionForm(request.POST)
    if request.method == 'POST':
        if studysessionform.is_valid():
            session_saver = Session()
            session_saver.sessions = studysessionform.cleaned_data['sessions']
            session_saver.save()
            group.study_sessions.add(session_saver)
            group.save()
            return HttpResponseRedirect(reverse('view_group', args=(group.id,)))
    else:
        studysessionform = StudySessionForm()

    return render(request, 'studysession.html', {'studysessionform': studysessionform})

class CourseView(generic.ListView):
    model = Course
    template_name = 'courses/CourseView.html'
    context_object_name = 'CourseGroupsList'
    fields = ['course_name']

    def get_queryset(self):
        return Course.objects.all()


class UserView(generic.ListView):
    model = UserT
    template_name = 'Users/UserView.html'
    context_object_name = 'UserList'

    def get_queryset(self):
        return UserT.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['UserCourses'] = Course.objects.all()
        context['UserGroups'] = Group.objects.all()
        # Add any other variables to the context here
        return context


# class UserForm(generic.CreateView):
#     model = User
#     template_name = 'Users/UserForm.html'
#     context_object_name = 'username'
#     def get_queryset(self):
# #         return User.objects.all()


@login_required
def UserPage(request):
    user, created = UserT.objects.get_or_create(email=request.user.email)
    user.email = request.user.email
    user.username = user.email
    user.save()
    print("in User View")
    print(user.CourseList)
    return render(request, 'Users/UserView.html',
                  {'user_courses': user.CourseList.all(), 'user_groups': user.GroupsList.all(), 'name': user.username, 'friends': user.friends_list.all()})


@login_required()
def eval_user(request):
    newuser, created = UserT.objects.get_or_create(email=request.user.email)
    newuser.email = request.user.email
    newuser.username = newuser.email
    newuser.save()

    return render(request, 'studybuddy.html', {'name': newuser.username})
    # return render(request, 'setusername.html', {'name' : newuser.username, 'username_set' : newuser.has_set_username}) #return to a different URL to process account creation


# def AddCourse(request):
#     user, created = User.objects.get_or_create(email=request.user.email)
#
@login_required()
def JoinGroup(request, group_ID):
    group = Group.objects.get(id=group_ID)
    user = UserT.objects.get(email=request.user.email)
    group.member_list.add(user)
    user.GroupsList.add(group)
    user.save()
    group.save()
    return render(request, 'Users/UserView.html',
                  {'user_courses': user.CourseList.all(), 'user_groups': user.GroupsList.all(), 'name': user.username})


@login_required()
def CreateGroup(request, course_ID):
    group = Group()
    group.group_name = request.user.email + "'s group"
    group.save()
    user = UserT.objects.get(email=request.user.email)
    group.member_list.add(user)
    user.GroupsList.add(group)
    user.save()
    group.save()
    course = Course.objects.get(course_IDI=course_ID)
    print(course.groups_list.all())
    course.groups_list.add(group)
    course.save()
    #print(course.groups_list.all())
    return render(request, 'groups/GroupsView.html',
                  {'members_list': group.member_list.all(), 'courseID': course_ID, 'group_id': group.id})


def ViewGroup(request, group_ID):
    group = Group.objects.get(id=group_ID)
    return render(request, 'groups/GroupsView.html',
                  {'members_list': group.member_list.all(), 'group_id': group.id, 'study_sessions': group.study_sessions.all()})


def ViewCourse(request, course_ID, course_subject):
    base_url = "http://luthers-list.herokuapp.com/api/dept/"
    formatting = "?format=json"
    response = requests.get(base_url + course_subject + formatting).json()
    course_info = []
    #print("displaying course")
    #print(response[1]["course_number"])
    #print(len(course_ID))
    for i in range(len(response)):
        if(response[i]['course_number'] == int(course_ID)):
            course_info = response[i]
            #print("found a course")
    newcourse, created = Course.objects.get_or_create(course_IDI=course_ID)
    newcourse.course_sub = course_subject
    newcourse.course_IDI = course_ID
    # course_log = API call for this specific course
    newcourse.save()
    #print(newcourse.groups_list.all())
    return render(request, 'courses/CourseView.html',
                  {'course_groups': newcourse.groups_list.all(), 'courseID': course_ID, 'courseJSON': course_info})

def add_friend(request, user_email):
    user_to_add = UserT.objects.get(email = user_email)
    user_holding = UserT.objects.get(email = request.user.email)
    user_holding.friends_list.add(user_to_add)
    user_holding.save()
    return render(request, 'Users/UserView.html',
                  {'user_courses': user_holding.CourseList.all(), 'user_groups': user_holding.GroupsList.all(), 'name': user_holding.username,
                   'friends': user_holding.friends_list.all()})


@login_required()
def AddCourse(request, course_ID):
    course = Course.objects.get(course_IDI=course_ID)
    user = UserT.objects.get(email=request.user.email)
    user.CourseList.add(course)
    user.save()

    return render(request, 'Users/UserView.html',
                  {'user_courses': user.CourseList.all(), 'user_groups': user.GroupsList.all(), 'name': user.username})


# def ViewCourse(request):
#     newcourse, created = Course.objects.get_or_create()

# def display_user(request, username):
# display_name = User.objects.all()[username]
# return render(request, 'studybuddy.html', {'name': display_name})

# def CreateCourses(request):
#     #info = urllib.request.urlopen('http://luthers-list.herokuapp.com/api/deptlist/?format=json', data=None)
#     #departments = info.read()
#     #dept = eval(departments)
#     #for i in range(len(dept)):
#     #    dept[i].save()
#
#     #return render(request, 'departments.html', {})
#     response = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
#     #print(response)
#    # print(response[0]['subject'])
#     # list of department
#     # per department, a list of all courses
#     course_list = {}
#     course_list2 = []
#     response2 = response[0]['subject']
#     base_url = "http://luthers-list.herokuapp.com/api/dept/"
#     formatting = "?format=json"
#     temp_list = []
#     for i in range(len(response)):
#         response2 = requests.get(base_url + response[i]['subject'] + formatting).json()
#         for l in range(len(response2)):
#             if response2[l]['description'] not in temp_list:
#                 create_course(response2[l])
#                 temp_list.append(response2[l]['description'])
#                 course_list2.append(response2[l])
#         course_list[response[i]['subject']] = course_list2
#         course_list2 = []
#
#     print(type(list(Course.objects.all())))
#     print(list(Course.objects.all())[8])
#
#     return render(request, 'departments.html', {'response': response, 'response2': list(Course.objects.all())})
#
# def create_course(list):
#     newcourse, created = Course.objects.get_or_create(course_name = list['description'])
#     newcourse.course_name = list['description']
#     newcourse.course_log = list
#     newcourse.save()
