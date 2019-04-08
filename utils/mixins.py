import json

from django.http import HttpResponseServerError, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bb_user.models import AuthToken
from utils.exceptions import RequestDecodeFailedAPIError, APIError


class APIMixin(object):

    def get_parameters(self, request):

        parameters = {}

        try:
            if request.method in ('POST', 'PUT'):
                parameters = json.loads(request.body)

            if request.method == 'GET':
                parameters = request.GET

        except ValueError as e:
            raise RequestDecodeFailedAPIError(e)

        return parameters

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):

        try:
            result = super(APIMixin, self).dispatch(request, parameters=self.get_parameters(request), *args, **kwargs)

        except APIError as e:
            return self.render_to_response({
                'success': False,
                'error': {
                    'code': e.code,
                    'message': e.message
                }
            })

        except Exception:
            return self.render_to_response({
                'success': False,
                'error': {
                    'code': 'internal_error',
                    'message': 'An internal error occurred.'
                }
            }, response_class=HttpResponseServerError)

        return self.render_to_response({
            'success': True,
            'result': result
        })

    def render_to_response(self, result, response_class=HttpResponse):
        return response_class(json.dumps(result), content_type='application/json')


class APIPermissionsMixin:
    def has_permissions(self, access_token):
        access_token = AuthToken.objects.get(access_token=access_token)
        user = access_token.user
        if user.is_superuser:
            return True
        return False
