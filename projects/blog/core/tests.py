from django.test import TestCase
from django.urls import reverse


class APITest(TestCase):

    # python manage.py dumpdata -o text_fixtures.json --exclude=contenttypes
    fixtures = ['text_fixtures.json']

    def setUp(self):
        self.token = self.test_get_token()

    def test_get_token(self, username='Bret', password='leanne@1234'):
        request_data = {'username': username, 'password': password}
        response = self.client.post(reverse('api-token'), data=request_data)
        self.assertEqual(response.status_code, 200)
        return 'Token {}'.format(response.data['token'])

