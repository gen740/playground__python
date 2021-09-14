"""
This type stub file was generated by pyright.
"""

UserModel = ...
class BaseBackend:
    def authenticate(self, request, **kwargs):
        ...
    
    def get_user(self, user_id):
        ...
    
    def get_user_permissions(self, user_obj, obj=...):
        ...
    
    def get_group_permissions(self, user_obj, obj=...):
        ...
    
    def get_all_permissions(self, user_obj, obj=...):
        ...
    
    def has_perm(self, user_obj, perm, obj=...):
        ...
    


class ModelBackend(BaseBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """
    def authenticate(self, request, username=..., password=..., **kwargs):
        ...
    
    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        ...
    
    def get_user_permissions(self, user_obj, obj=...):
        """
        Return a set of permission strings the user `user_obj` has from their
        `user_permissions`.
        """
        ...
    
    def get_group_permissions(self, user_obj, obj=...):
        """
        Return a set of permission strings the user `user_obj` has from the
        groups they belong.
        """
        ...
    
    def get_all_permissions(self, user_obj, obj=...):
        ...
    
    def has_perm(self, user_obj, perm, obj=...):
        ...
    
    def has_module_perms(self, user_obj, app_label):
        """
        Return True if user_obj has any permissions in the given app_label.
        """
        ...
    
    def with_perm(self, perm, is_active=..., include_superusers=..., obj=...):
        """
        Return users that have permission "perm". By default, filter out
        inactive users and include superusers.
        """
        ...
    
    def get_user(self, user_id):
        ...
    


class AllowAllUsersModelBackend(ModelBackend):
    def user_can_authenticate(self, user):
        ...
    


class RemoteUserBackend(ModelBackend):
    """
    This backend is to be used in conjunction with the ``RemoteUserMiddleware``
    found in the middleware module of this package, and is used when the server
    is handling authentication outside of Django.

    By default, the ``authenticate`` method creates ``User`` objects for
    usernames that don't already exist in the database.  Subclasses can disable
    this behavior by setting the ``create_unknown_user`` attribute to
    ``False``.
    """
    create_unknown_user = ...
    def authenticate(self, request, remote_user):
        """
        The username passed as ``remote_user`` is considered trusted. Return
        the ``User`` object with the given username. Create a new ``User``
        object if ``create_unknown_user`` is ``True``.

        Return None if ``create_unknown_user`` is ``False`` and a ``User``
        object with the given username is not found in the database.
        """
        ...
    
    def clean_username(self, username):
        """
        Perform any cleaning on the "username" prior to using it to get or
        create the user object.  Return the cleaned username.

        By default, return the username unchanged.
        """
        ...
    
    def configure_user(self, request, user):
        """
        Configure a user after creation and return the updated user.

        By default, return the user unmodified.
        """
        ...
    


class AllowAllUsersRemoteUserBackend(RemoteUserBackend):
    def user_can_authenticate(self, user):
        ...
    

