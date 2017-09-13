import tortilla

from .exceptions import api_exception_register, APIClientError


class Resource(object):

    def __init__(self, resource):
        self._resource = resource

    @property
    def resource(self):
        return self._resource

    def all(self):
        return self.process_result(self.resource.get())

    def get(self, id):
        return self.process_result(self.resource.get(id))

    def process_result(self, result):

        if not result['success']:
            raise api_exception_register.get(result['error']['code'], APIClientError)(result['error']['message'])

        return result['result']


class Post(Resource):

    @property
    def resource(self):
        return self._resource.posts


class BackendAPIClient(object):

    def __init__(self, api_url):

        self.api_url = api_url
        self.resource = tortilla.wrap(api_url)

        self.post = Post(self.resource)
