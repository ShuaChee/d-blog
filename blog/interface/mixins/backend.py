from django.conf import settings

from utils.api_clients.backend import BackendAPIClient


class BackendMixin(object):

    @property
    def backend(self):
        return BackendAPIClient(settings.BACKEND_API_URL)
