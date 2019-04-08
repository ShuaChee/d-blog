from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):

    subject = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta(object):
        app_label = 'bb_post'
        db_table = 'post'
