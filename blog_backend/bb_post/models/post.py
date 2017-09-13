from django.db import models


class Post(models.Model):

    subject = models.TextField()
    content = models.TextField()

    class Meta(object):
        app_label = 'bb_post'
        db_table = 'post'
