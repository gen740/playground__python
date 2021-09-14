"""
This type stub file was generated by pyright.
"""

from django import forms
from django.contrib.auth.models import User

UserModel = ...
class ReadOnlyPasswordHashWidget(forms.Widget):
    template_name = ...
    read_only = ...
    def get_context(self, name, value, attrs):
        ...
    


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class UsernameField(forms.CharField):
    def to_python(self, value):
        ...
    
    def widget_attrs(self, widget):
        ...
    


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = ...
    password1 = ...
    password2 = ...
    class Meta:
        model = User
        fields = ...
        field_classes = ...
    
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def clean_password2(self):
        ...
    
    def save(self, commit=...):
        ...
    


class UserChangeForm(forms.ModelForm):
    password = ...
    class Meta:
        model = User
        fields = ...
        field_classes = ...
    
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = ...
    password = ...
    error_messages = ...
    def __init__(self, request=..., *args, **kwargs) -> None:
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        ...
    
    def clean(self):
        ...
    
    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        ...
    
    def get_user(self):
        ...
    
    def get_invalid_login_error(self):
        ...
    


class PasswordResetForm(forms.Form):
    email = ...
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=...):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        ...
    
    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        ...
    
    def save(self, domain_override=..., subject_template_name=..., email_template_name=..., use_https=..., token_generator=..., from_email=..., request=..., html_email_template_name=..., extra_email_context=...):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        ...
    


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = ...
    new_password1 = ...
    new_password2 = ...
    def __init__(self, user, *args, **kwargs) -> None:
        ...
    
    def clean_new_password2(self):
        ...
    
    def save(self, commit=...):
        ...
    


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = ...
    old_password = ...
    field_order = ...
    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        ...
    


class AdminPasswordChangeForm(forms.Form):
    """
    A form used to change the password of a user in the admin interface.
    """
    error_messages = ...
    required_css_class = ...
    password1 = ...
    password2 = ...
    def __init__(self, user, *args, **kwargs) -> None:
        ...
    
    def clean_password2(self):
        ...
    
    def save(self, commit=...):
        """Save the new password."""
        ...
    
    @property
    def changed_data(self):
        ...
    

