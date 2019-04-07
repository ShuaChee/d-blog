import json
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from bb_user.models import User
from bb_user.api.views import UserCreateView


class UserLoginViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserCreateView.as_view()

    def tearDown(self):
        pass

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
