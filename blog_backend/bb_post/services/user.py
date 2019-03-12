from bb_user.models import User


def create(name, email):
    User.objects._create_user(username=name, email=email)
