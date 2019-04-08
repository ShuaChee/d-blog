from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bb_post.api.forms.post import CreateForm
from bb_post.api.mixins import PostAPIMixin
from bb_post.api.serializers.post import serialize as serialize_post
from bb_post.models import Post
from bb_post.api.serializers.post import PostSerializer
from utils.exceptions import RequestValidationFailedAPIError
from utils.mixins import APIMixin

import bb_post.services.post


class PostView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()

    '''def post(self, request):
        serializer = PostSerializer(data=request.data, )
        if serializer.is_valid():
            post = serializer.save()
            return Response(post)
        else:
            return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)'''



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
