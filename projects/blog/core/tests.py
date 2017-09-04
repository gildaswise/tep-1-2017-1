from django.test import TestCase
from django.urls import reverse


# Para testar, basta chamar
# python manage.py tests core.tests
class APITest(TestCase):

    # python manage.py dumpdata -o text_fixtures.json --exclude=contenttypes
    fixtures = ['text_fixtures.json']

    def setUp(self):
        self.token = self.get_token()

    def get_token(self, username='Bret', password='leanne@1234'):
        request_data = {'username': username, 'password': password}
        response = self.client.post(reverse('api-token'), data=request_data)
        self.assertEqual(response.status_code, 200)
        return 'Token {}'.format(response.data['token'])

    # Route integrity tests

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        response = self.client.get(reverse('user-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_profile_list(self):
        response = self.client.get(reverse('profile-list'))
        self.assertEqual(response.status_code, 200)

    def test_profile_detail(self):
        response = self.client.get(reverse('profile-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_post_list(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        response = self.client.get(reverse('post-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_comment_list(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, 200)

    def test_comment_detail(self):
        response = self.client.get(reverse('comment-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    # Permission tests
    # HTTP_AUTHORIZATION = self.token

    # def test_profile_detail_unauthorized(self):
    #     request_data = {"id": 1,
    #                     "username": "Bret",
    #                     "email": "Sincere@april.biz",
    #                     "name": "Leanne Graham"}
    #     response = self.client.put(reverse('profile-detail', args=(1,)),
    #                                data=request_data)
    #     self.assertEqual(response.status_code, 401)
    #     response = self.client.put(reverse('profile-detail', args=(1,)),
    #                                data=request_data,
    #                                HTTP_AUTHORIZATION=self.token)
    #     self.assertEqual(response.status_code, 200)
