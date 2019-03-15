from bb_post.models import Post


def create(subject, content):
    return Post.objects.create(subject=subject, content=content)
