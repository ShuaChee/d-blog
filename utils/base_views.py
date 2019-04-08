import json
from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bb_user.models import AuthToken


class APIView(View):
    user_model = get_user_model()
    need_auth = False

    def get_access_token(self, request):
        try:
            access_token = request.META['HTTP_AUTHORIZATION']
        except KeyError:
            access_token = None
        return access_token

    def get_user_session(self, access_token):
        try:
            session = AuthToken.objects.get(access_token=access_token)
        except AuthToken.DoesNotExist:
            return False
        return session

    def access_token_is_expired(self, access_token):
        session = AuthToken.objects.get(access_token=access_token)
        if session.expired_at < datetime.now(timezone.utc):
            return True
        return False

    def get_parameters(self, request):
        parameters = {}
        try:
            if request.method in ('POST', 'PUT'):
                parameters = json.loads(request.body)

            if request.method == 'GET':
                if not request.GET._mutable:
                    request.GET._mutable = True
                parameters = request.GET

        except:
            return JsonResponse({'Message': 'Load Data Error'}, status=500)

        return parameters

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.access_token = self.get_access_token(request)
        self.session = self.get_user_session(self.access_token)
        if self.need_auth:
            if not self.session and self.access_token:
                return JsonResponse({'Message': 'Invalid Token'}, status=403)
            if self.access_token and self.access_token_is_expired(self.access_token):
                return JsonResponse({'Message': 'Relogin Please'}, status=403)
        # try:
        result = super(APIView, self).dispatch(request, parameters=self.get_parameters(request), *args, **kwargs)
        # except:
        # return JsonResponse({'Message': 'Something wrong'}, status=500)
        return result
