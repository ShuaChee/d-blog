from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    # gravatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.username, self.user_email)
