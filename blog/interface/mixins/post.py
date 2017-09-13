from django.http import HttpResponseForbidden

from utils.api_clients.backend import PostUnknownAPIClientError


class PostMixin(object):

    post = None

    def dispatch(self, *args, **kwargs):

        try:
            self.post = self.backend.post.get(kwargs['post_id'])

        except PostUnknownAPIClientError:
            return HttpResponseForbidden('403 Forbidden')

        return super(PostMixin, self).dispatch(*args, **kwargs)
