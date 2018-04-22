
class NameError(Exception)
    """ Base class for all errors
    """
    def __repr__(self):
        """ Pretty print this error
        """
        return str(self)

class NameHttpError(NameError):
    """ Base class for all HTTP/network related errors
    """
    response_code    = -1
    response_message = ''
    response_headers = {}
    response_body    = ''

    def __init__(self, response):
        """ Construct a triton http error which captures request (and
            optionally response information from a failed request.
        """
        NameError.__init__(self, 'Request failed.')
        self.response_code    = response.status
        self.response_message = response.reason
        self.response_headers = response.headers
        self.response_body    = response.body

    @staticmethod
    def format_headers(headers):
        """ Helper method to pretty print header dictionaries
        """
        if not headers:
            return '< none >'
        prefix = '\n' + (' ' * 23)
        return prefix.join(['%s: %s' % p for p in headers.items() ])

    def __str__(self):
        """ Pretty print this error
        """
        # Was returning self.response_body also, but this is unsafe as it can have characters that cause
        # the low level logging routines to throw exceptions.
        return ( '%s <\n'
                 '    response_status  : %s %s\n'
                 '    response_headers : %s\n'
                 '>' ) % (
            type(self).__name__,
            self.response_code,
            self.response_message,
            self.format_headers(self.response_headers),
            )

class NameNotFound(NameHttpError):
    """ Raised when Name says we've asked for a non-existent entity.
    """
    pass

class NameUnauthorized(NameHttpError):
    """ Raised when Name refuses us access.
    """
    pass

class NameBadRequest(NameHttpError):
    """ Raised when Name complains about input we gave it.
    """
    pass

class NameServerError(NameHttpError):
    """ Raised when triton does something we don't expect
    """
    pass


class NameParseError(NameError):
    """ Raised when server sends content we don't understand
    """
    def __init__(self, message, value):
        """ Constructor.  Set the error message and remember the
            problem value
        """
        NameError.__init__(self, message)
        self.message = message
        self.value = value

    def __str__(self):
        """ Pretty print this error
        """
        return '%s: %s\n    %s' % (
            type(self),
            self.message,
            '\n    '.join([line for line in self.value.split('\n')]))

