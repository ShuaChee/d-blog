class APIError(Exception):
    code = None


class RequestAPIError(APIError):
    pass


class RequestDecodeFailedAPIError(RequestAPIError):
    code = 'request_decode_failed'


class RequestValidationFailedAPIError(RequestAPIError):
    code = 'request_validation_failed'
