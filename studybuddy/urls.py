from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView

from django.contrib.auth.views import LogoutView
urlpatterns = [
    # Make it course name + Course ID
    #path('studybuddy/', TemplateView.as_view(template_name="studybuddy.html")),
    #path('studybuddy/', views.eval_user, name="create"),
    path('', views.studybuddy, name='studybuddy'),
    #path('group/form/view/', views.GroupView.as_view(), name='group'),
    #path('group/form/', views.GroupViewForm.as_view(), name='group_form'),
    # path('course/', views.CourseView.as_view(), name='course_view'),
    path('user/', views.UserPage, name="user"),
    path('dep/', views.getAllDepartments, name="dep"),
    path('course/<str:course_ID>/<str:course_subject>', views.ViewCourse, name="course"),
    path('course/<str:course_ID>/addc/', views.AddCourse, name="add_course"),
    path('course/<str:course_ID>/addg/', views.CreateGroup, name="add_group"),
    path('group/<int:group_ID>/', views.JoinGroup, name="join_group"),
    path('group/<int:group_ID>/view', views.ViewGroup, name="view_group"),
    path('group/<int:group_ID>/view/studysession', views.StudySessionView, name="studysession"),
    path('friend/<str:user_email>', views.add_friend, name="add_friend"),
    path('avatar/', include('avatar.urls')),
    # path('adm/addcourses', views.CreateCourses, name='admincreate'),
    # path('logout', LogoutView.as_view()),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)