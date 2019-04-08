import json
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token

from bb_user.models import User
from bb_user.api.views import UserCreateView
from bb_user.api.views import UserActivateView
from bb_user.api.views import UserResetPasswordView


class UserCreateViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserCreateView.as_view()

    def test_create_user_view_success(self):
        request = self.factory.post('create/', json.dumps({
            'username': 'admin',
            'password': 'admin',
            'confirm_password': 'admin',
            'email': 'admin@admin.com'
        }), content_type='application/json')
        response = self.view(request)
        self.assertEqual(201, response.status_code)

    def test_user_create_view_fail_wrong_password_confirmation(self):
        request = self.factory.post('create/', json.dumps({
            'username': 'admin',
            'password': 'admin',
            'confirm_password': 'asdasd',
            'email': 'admin@admin.com'
        }), content_type='application/json')
        response = self.view(request)
        self.assertEqual(400, response.status_code)

    def test_user_create_view_form_filling(self):
        request = self.factory.post('create/', json.dumps({
            'username': '',
            'password': '',
            'confirm_password': '',
            'email': 'admin@.com'
        }), content_type='application/json')
        response = self.view(request)
        self.assertEqual(400, response.status_code)

    def test_user_create_view_fail_already_exists(self):
        user = User.objects.create(username='admin', password='admin', email='admin@admin.com')
        user.save()
        request = self.factory.post('create/', json.dumps({
            'username': 'admin',
            'password': 'admin',
            'confirm_password': 'admin',
            'email': 'admin@admin.com'
        }), content_type='application/json')
        response = self.view(request)

        self.assertEqual(400, response.status_code)


class UserActivateViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.activate_view = UserActivateView.as_view()
        self.user = User.objects.create(username='admin', password='admin', email='admin@admin.com')
        self.token = Token.objects.create(user=self.user)

    def test_user_activation_fail(self):
        request = self.factory.get('activate/?t=wrong_token')
        response = self.activate_view(request)
        self.assertEqual(400, response.status_code)

    def test_user_activation_success(self):
        request = self.factory.get('activate/?t='+self.token.key)
        response = self.activate_view(request)
        self.assertEqual(200, response.status_code)


class UserResetPasswordViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserResetPasswordView.as_view()
        self.user = User.objects.create_user(username='admin', email='email@admin.com', password='admin')

    def test_user_reset_password_get_reset_link_fail(self):
        request = self.factory.get('reset/?email=wrong_email')
        response = self.view(request)
        response.render()
        response = json.loads(response.content)

        self.assertEqual('User not found', response['user'])

    def test_user_reset_password_get_reset_link_success(self):
        request = self.factory.get('reset/?email=email@admin.com')
        response = self.view(request)
        self.assertEqual(200, response.status_code)
        response.render()
        response = json.loads(response.content)
        self.assertEqual('Reset link sent', response[0]['Message'])

    def test_user_reset_password_fail_wrong_token(self):
        request = self.factory.post('reset/', json.dumps({
            'reset_token': '',
            'password': 'password',
            'confirm_password': 'password'
        }), content_type='application/json')
        response = self.view(request)
        response.render()
        response = json.loads(response.content)

        self.assertEqual('Invalid token', response['reset_token'])

    def test_user_reset_password_success(self):
        token = Token.objects.create(user=self.user)
        request = self.factory.post('reset/', json.dumps({
            'reset_token': token.key,
            'password': 'password',
            'confirm_password': 'password'
        }), content_type='application/json')
        response = self.view(request)
        response.render()
        response = json.loads(response.content)

        self.assertEqual('Password changed', response['Message'])


class UserLogoutViewTestCase(APITestCase):

    def setUp(self):
        pass

    def test_user_logout(self):
        pass


class UserBlockViewTestCase(APITestCase):

    def setUp(self):
        pass

