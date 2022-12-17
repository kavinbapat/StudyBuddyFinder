import requests
from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    # Testing if client can successfully retrieve the studybuddy URL
    def test_link(self):
        response = self.client.get(reverse('studybuddy'))
        self.assertEqual(response.status_code, 200)

    def test_department_render(self):
        response = self.client.get(reverse('dep'))
        self.assertEqual(response.status_code, 200)


class LoginTests(TestCase):
    # test page to see if it has the login option
    def test_loging_accessibility(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 302)


class APITests(TestCase):
    # Testing if the API can successfully reach its appropiate end points and gather appropiate data

    def test_api_source(self):
        response = requests.get('http://luthers-list.herokuapp.com/api/deptlist')
        self.assertEqual(response.status_code, 200)

    def test_api_dept_pull(self):
        response = requests.get('http://luthers-list.herokuapp.com/api/deptlist').json()
        self.assertEqual(response[0]['subject'], 'ACCT')

    def test_api_course_pull(self):
        response = requests.get('http://luthers-list.herokuapp.com/api/dept/ACCT').json()
        response2 = response[0]['description']
        self.assertEqual(response2, 'Introductory Accounting I')
