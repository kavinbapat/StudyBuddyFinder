from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room


# """/***************************************************************************************
# *  REFERENCES
# *  Title: How to Build Chat into Django Applications with Twilio Programmable Chat
# *  Author: Kevin Ndung'U
# *  Date: November 11, 2022
# *  URL: https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html
# *
# *  
# *  Repository: chat-django
# *  Author: Kevin Gathuku (kevgathuku)
# *  Date: November 11, 2022
# *  URL: https://github.com/kevgathuku/chat-django
# *
# *  Description: Utilized to create the chat room view
# *
# ***************************************************************************************/"""
# @login_required
def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


# @login_required
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'chat/room_detail.html', {'room': room})


def swap(request):
    return HttpResponseRedirect("sb/")


@login_required
def create_room(request, slug):
    room, create = Room.objects.get_or_create(slug=(request.user.email + slug))
    room.save()
    room.name = request.user.email + slug + "'s room"
    room.description = request.user.email + slug + "'s room"
    room.save()
    return render(request, 'chat/room_detail.html', {'room': room})


def token(request):
    identity = request.GET.get('identity', request.user.email)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token1 = AccessToken(account_sid, api_key, api_secret, identity=identity)

    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token1.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token1.to_jwt()
    }

    return JsonResponse(response)
