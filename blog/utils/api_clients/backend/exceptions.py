api_exception_register = dict()


class APIClientErrorRegistry(type):

    """
    Registers error codes and class signatures into a global exception register
    which is able to map error codes to a specific exception.
    """

    def __new__(cls, name, bases, attrs):
        """
        Put the error code and class signature into the register when the class
        is defined.
        """

        exception_class = super(APIClientErrorRegistry, cls).__new__(cls, name, bases, attrs)

        # Register the error code with this class signature
        if exception_class.code is not None:
            api_exception_register[exception_class.code] = exception_class

        return exception_class


class APIClientError(Exception):

    """
    An all purpose exception which is used when something went wrong with the
    API client, either during the request or during the response.
    """

    __metaclass__ = APIClientErrorRegistry

    code = 'internal_error'


class PostUnknownAPIClientError(APIClientError):
    code = 'post_unknown'
