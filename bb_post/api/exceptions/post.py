from utils.api.exceptions import APIError


class PostAPIError(APIError):
    pass


class PostUnknownAPIError(PostAPIError):
    code = 'post_unknown'
