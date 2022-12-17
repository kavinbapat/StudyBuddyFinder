# """/***************************************************************************************
# *  REFERENCES
# *  Title: How to Build Chat into Django Applications with Twilio Programmable Chat
# *  Author: Kevin Ndung'U
# *  Date: November 11, 2022
# *  URL: https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html
# *  
# *  Repository: chat-django
# *  Author: Kevin Gathuku (kevgathuku)
# *  Date: November 11, 2022
# *  URL: https://github.com/kevgathuku/chat-django
# *
# *  Description: Utilized to create the chat room urls
# *
#***************************************************************************************/"""
# chat/urls.py

from django.urls import path, include
from django.urls import re_path
from . import views

urlpatterns = [
    path("", views.swap, name="redir"),
    path('chat/', views.all_rooms, name="all_rooms"),
    re_path(r'^$', views.all_rooms, name="all_rooms"),
    re_path(r'token$', views.token, name="token"),
    #re_path(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
    path('create/<str:slug>', views.create_room, name="create_room"),
    path('rooms/<str:slug>/', views.room_detail, name="room_deets"),
]
