
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
# *  Description: Utilized to create the chat room dynamic elements
# *
# ***************************************************************************************/"""

from django.test import TestCase
from django.urls import reverse
from .models import Room

class BasicChatTests(TestCase):
    # tests if client can reach All room page
    def test_allrooms_by_name(self):
        response = self.client.get(reverse('all_rooms'))
        self.assertEqual(response.status_code, 200)


    def test_allroom_template_name_correct(self):  
        response = self.client.get(reverse("all_rooms"))
        self.assertTemplateUsed(response, "chat/index.html")



class AllRoomTest(TestCase):
    #tests related to all room page
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(
        name='room 1',
        slug='room-1',
        description='This is the 1st room')

        Room.objects.create(
        name='room 2',
        slug='room-2',
        description='This is the 2nd room')


    def test_all_rooms_are_rendered_in_homepage(self):

        response = self.client.get(reverse('all_rooms'))

        self.assertContains(response, 'room 1')
        self.assertContains(response, 'room 2')

    def number_of_test(self):

        number=Room.objects.count();


class RoomDetailTest(TestCase):
#tests related to room detail page
    @classmethod
    def setUpTestData(cls):
        room_5 = Room.objects.create(
        name='room 5',
        slug='room-5',
        description='This is the 5-room'
        )


    def test_roomdetail_by_name(self):
        response = self.client.get(reverse('room_detail', args=[room_5.slug]))
        self.assertEqual(response.status_code, 200)


    def test_roomdetail_template_name_correct(self):  
        response = self.client.get(reverse('room_detail', args=[room_5.slug]))
        self.assertTemplateUsed(response, "chat/room_detail.html")


    def test_room_details_url_correct(self):
        response = self.client.get('/rooms/{}/'.format(room_5.slug))
        self.assertEqual(response.status_code, 200)


    def test_room_details_are_present_in_room_page(self):
        response = self.client.get('/rooms/{}/'.format(room_5.slug))
        self.assertContains(response, room_5.name)
        self.assertContains(response, room_5.description)







