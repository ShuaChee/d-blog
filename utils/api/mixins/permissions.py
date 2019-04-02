from bb_user.models import AuthToken



class APIPermissionsMixin:
    def has_permissions(self, access_token):
        access_token = AuthToken.objects.get(access_token=access_token)
        user = access_token.user
        if user.is_superuser:
            return True
        return False


