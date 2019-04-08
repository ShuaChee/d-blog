from rest_framework import serializers
from bb_post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('subject', 'content', 'author')


def serialize(post):

    serialized_post = serialize_id(post)

    serialized_post.update({
        'subject': post.subject,
        'content': post.content
    })

    return serialized_post


def serialize_id(post):
    return {
        'id': post.id
    }
