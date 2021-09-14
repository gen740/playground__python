"""
This type stub file was generated by pyright.
"""

import warnings
from contextlib import ContextDecorator
from decimal import Decimal, ROUND_UP
from django.utils.autoreload import autoreload_started, file_changed
from django.utils.deprecation import RemovedInDjango40Warning
from django.utils.functional import lazy
from django.utils.regex_helper import _lazy_re_compile

"""
Internationalization support.
"""
LANGUAGE_SESSION_KEY = ...
class TranslatorCommentWarning(SyntaxWarning):
    ...


class Trans:
    """
    The purpose of this class is to store the actual translation function upon
    receiving the first call to that function. After this is done, changes to
    USE_I18N will have no effect to which function is served upon request. If
    your tests rely on changing USE_I18N, you can delete all the functions
    from _trans.__dict__.

    Note that storing the function with setattr will have a noticeable
    performance effect, as access to the function goes the normal path,
    instead of using __getattr__.
    """
    def __getattr__(self, real_name):
        ...
    


_trans = ...
def gettext_noop(message):
    ...

def ugettext_noop(message):
    """
    A legacy compatibility wrapper for Unicode handling on Python 2.
    Alias of gettext_noop() since Django 2.0.
    """
    ...

def gettext(message):
    ...

def ugettext(message):
    """
    A legacy compatibility wrapper for Unicode handling on Python 2.
    Alias of gettext() since Django 2.0.
    """
    ...

def ngettext(singular, plural, number):
    ...

def ungettext(singular, plural, number):
    """
    A legacy compatibility wrapper for Unicode handling on Python 2.
    Alias of ngettext() since Django 2.0.
    """
    ...

def pgettext(context, message):
    ...

def npgettext(context, singular, plural, number):
    ...

gettext_lazy = ...
pgettext_lazy = ...
def ugettext_lazy(message):
    """
    A legacy compatibility wrapper for Unicode handling on Python 2. Has been
    Alias of gettext_lazy since Django 2.0.
    """
    ...

def lazy_number(func, resultclass, number=..., **kwargs):
    ...

def ngettext_lazy(singular, plural, number=...):
    ...

def ungettext_lazy(singular, plural, number=...):
    """
    A legacy compatibility wrapper for Unicode handling on Python 2.
    An alias of ungettext_lazy() since Django 2.0.
    """
    ...

def npgettext_lazy(context, singular, plural, number=...):
    ...

def activate(language):
    ...

def deactivate():
    ...

class override(ContextDecorator):
    def __init__(self, language, deactivate=...) -> None:
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    


def get_language():
    ...

def get_language_bidi():
    ...

def check_for_language(lang_code):
    ...

def to_language(locale):
    """Turn a locale name (en_US) into a language name (en-us)."""
    ...

def to_locale(language):
    """Turn a language name (en-us) into a locale name (en_US)."""
    ...

def get_language_from_request(request, check_path=...):
    ...

def get_language_from_path(path):
    ...

def get_supported_language_variant(lang_code, *, strict=...):
    ...

def templatize(src, **kwargs):
    ...

def deactivate_all():
    ...

def get_language_info(lang_code):
    ...

trim_whitespace_re = ...
def trim_whitespace(s):
    ...

def round_away_from_one(value):
    ...
