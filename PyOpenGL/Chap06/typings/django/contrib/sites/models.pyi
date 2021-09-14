"""
This type stub file was generated by pyright.
"""

from django.db import models

SITE_CACHE = ...
class SiteManager(models.Manager):
    use_in_migrations = ...
    def get_current(self, request=...):
        """
        Return the current Site based on the SITE_ID in the project's settings.
        If SITE_ID isn't defined, return the site with domain matching
        request.get_host(). The ``Site`` object is cached the first time it's
        retrieved from the database.
        """
        ...
    
    def clear_cache(self):
        """Clear the ``Site`` object cache."""
        ...
    
    def get_by_natural_key(self, domain):
        ...
    


class Site(models.Model):
    domain = ...
    name = ...
    objects = ...
    class Meta:
        db_table = ...
        verbose_name = ...
        verbose_name_plural = ...
        ordering = ...
    
    
    def __str__(self) -> str:
        ...
    
    def natural_key(self):
        ...
    


def clear_site_cache(sender, **kwargs):
    """
    Clear the cache (if primed) each time a site is saved or deleted.
    """
    ...

