from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # user_email = models.EmailField(unique=True)
    # user_name = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    # verified = models.BooleanField(default=False)
    # gravatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.username, self.email)


class UserSessions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=200)
    expired_at = models.DateTimeField(default=datetime.now() + timedelta(days=30))
