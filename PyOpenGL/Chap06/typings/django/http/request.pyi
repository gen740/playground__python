"""
This type stub file was generated by pyright.
"""

from urllib.parse import parse_qsl
from django.utils.datastructures import CaseInsensitiveMapping, MultiValueDict
from django.utils.functional import cached_property
from django.utils.http import parse_qsl
from django.utils.inspect import func_supports_parameter

if (not func_supports_parameter(parse_qsl, 'max_num_fields') or not func_supports_parameter(parse_qsl, 'separator')):
    ...
RAISE_ERROR = ...
host_validation_re = ...
class UnreadablePostError(OSError):
    ...


class RawPostDataException(Exception):
    """
    You cannot access raw_post_data from a request that has
    multipart/* POST data if it has been accessed via POST,
    FILES, etc..
    """
    ...


class HttpRequest:
    """A basic HTTP request."""
    _encoding = ...
    _upload_handlers = ...
    def __init__(self) -> None:
        ...
    
    def __repr__(self):
        ...
    
    @cached_property
    def headers(self):
        ...
    
    @cached_property
    def accepted_types(self):
        """Return a list of MediaType instances."""
        ...
    
    def accepts(self, media_type):
        ...
    
    def get_host(self):
        """Return the HTTP host using the environment or request headers."""
        ...
    
    def get_port(self):
        """Return the port number for the request as a string."""
        ...
    
    def get_full_path(self, force_append_slash=...):
        ...
    
    def get_full_path_info(self, force_append_slash=...):
        ...
    
    def get_signed_cookie(self, key, default=..., salt=..., max_age=...):
        """
        Attempt to return a signed cookie. If the signature fails or the
        cookie has expired, raise an exception, unless the `default` argument
        is provided,  in which case return that value.
        """
        ...
    
    def get_raw_uri(self):
        """
        Return an absolute URI from variables available in this request. Skip
        allowed hosts protection, so may return insecure URI.
        """
        ...
    
    def build_absolute_uri(self, location=...):
        """
        Build an absolute URI from the location and the variables available in
        this request. If no ``location`` is specified, build the absolute URI
        using request.get_full_path(). If the location is absolute, convert it
        to an RFC 3987 compliant URI and return it. If location is relative or
        is scheme-relative (i.e., ``//example.com/``), urljoin() it to a base
        URL constructed from the request variables.
        """
        ...
    
    @property
    def scheme(self):
        ...
    
    def is_secure(self):
        ...
    
    def is_ajax(self):
        ...
    
    @property
    def encoding(self):
        ...
    
    @encoding.setter
    def encoding(self, val):
        """
        Set the encoding used for GET/POST accesses. If the GET or POST
        dictionary has already been created, remove and recreate it on the
        next access (so that it is decoded correctly).
        """
        ...
    
    @property
    def upload_handlers(self):
        ...
    
    @upload_handlers.setter
    def upload_handlers(self, upload_handlers):
        ...
    
    def parse_file_upload(self, META, post_data):
        """Return a tuple of (POST QueryDict, FILES MultiValueDict)."""
        ...
    
    @property
    def body(self):
        ...
    
    def close(self):
        ...
    
    def read(self, *args, **kwargs):
        ...
    
    def readline(self, *args, **kwargs):
        ...
    
    def __iter__(self):
        ...
    
    def readlines(self):
        ...
    


class HttpHeaders(CaseInsensitiveMapping):
    HTTP_PREFIX = ...
    UNPREFIXED_HEADERS = ...
    def __init__(self, environ) -> None:
        ...
    
    def __getitem__(self, key):
        """Allow header lookup using underscores in place of hyphens."""
        ...
    
    @classmethod
    def parse_header_name(cls, header):
        ...
    


class QueryDict(MultiValueDict):
    """
    A specialized MultiValueDict which represents a query string.

    A QueryDict can be used to represent GET or POST data. It subclasses
    MultiValueDict since keys in such data can be repeated, for instance
    in the data from a form with a <select multiple> field.

    By default QueryDicts are immutable, though the copy() method
    will always return a mutable copy.

    Both keys and values set on this class are converted from the given encoding
    (DEFAULT_CHARSET by default) to str.
    """
    _mutable = ...
    _encoding = ...
    def __init__(self, query_string=..., mutable=..., encoding=...) -> None:
        ...
    
    @classmethod
    def fromkeys(cls, iterable, value=..., mutable=..., encoding=...):
        """
        Return a new QueryDict with keys (may be repeated) from an iterable and
        values from value.
        """
        ...
    
    @property
    def encoding(self):
        ...
    
    @encoding.setter
    def encoding(self, value):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __copy__(self):
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    def setlist(self, key, list_):
        ...
    
    def setlistdefault(self, key, default_list=...):
        ...
    
    def appendlist(self, key, value):
        ...
    
    def pop(self, key, *args):
        ...
    
    def popitem(self):
        ...
    
    def clear(self):
        ...
    
    def setdefault(self, key, default=...):
        ...
    
    def copy(self):
        """Return a mutable copy of this object."""
        ...
    
    def urlencode(self, safe=...):
        """
        Return an encoded string of all query string arguments.

        `safe` specifies characters which don't require quoting, for example::

            >>> q = QueryDict(mutable=True)
            >>> q['next'] = '/a&b/'
            >>> q.urlencode()
            'next=%2Fa%26b%2F'
            >>> q.urlencode(safe='/')
            'next=/a%26b/'
        """
        ...
    


class MediaType:
    def __init__(self, media_type_raw_line) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    
    @property
    def is_all_types(self):
        ...
    
    def match(self, other):
        ...
    


def bytes_to_text(s, encoding):
    """
    Convert bytes objects to strings, using the given encoding. Illegally
    encoded input characters are replaced with Unicode "unknown" codepoint
    (\ufffd).

    Return any non-bytes objects without change.
    """
    ...

def split_domain_port(host):
    """
    Return a (domain, port) tuple from a given host.

    Returned domain is lowercased. If the host is invalid, the domain will be
    empty.
    """
    ...

def validate_host(host, allowed_hosts):
    """
    Validate the given host for this site.

    Check that the host looks valid and matches a host or host pattern in the
    given list of ``allowed_hosts``. Any pattern beginning with a period
    matches a domain and all its subdomains (e.g. ``.example.com`` matches
    ``example.com`` and any subdomain), ``*`` matches anything, and anything
    else must match exactly.

    Note: This function assumes that the given host is lowercased and has
    already had the port, if any, stripped off.

    Return ``True`` for a valid host, ``False`` otherwise.
    """
    ...

def parse_accept_header(header):
    ...

