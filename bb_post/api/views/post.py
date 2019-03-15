from django.views.generic import View

from bb_post.api.forms.post import CreateForm
from bb_post.api.mixins import PostAPIMixin
from bb_post.api.serializers.post import serialize as serialize_post
from bb_post.models import Post
from utils.api.exceptions import RequestValidationFailedAPIError
from utils.api.mixins import APIMixin

import bb_post.services.post


class Collection(APIMixin, View):

    def get(self, request, parameters, *args, **kwargs):

        posts = Post.objects.all()

        return list(map(serialize_post, posts))

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if not form.is_valid():
            raise RequestValidationFailedAPIError(form.errors)

        post = bb_post.services.post.create(**form.cleaned_data)

        return serialize_post(post)


class Single(APIMixin, PostAPIMixin, View):

    def get(self, request, parameters, *args, **kwargs):
        return serialize_post(self.post)
