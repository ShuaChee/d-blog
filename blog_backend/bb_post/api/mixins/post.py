from bb_post.api.exceptions import PostUnknownAPIError
from bb_post.models import Post


class PostAPIMixin(object):

    post = None

    def dispatch(self, *args, **kwargs):

        try:
            self.post = Post.objects.get(id=kwargs['post_id'])

        except Post.DoesNotExist:
            raise PostUnknownAPIError()

        return super(PostAPIMixin, self).dispatch(*args, **kwargs)
