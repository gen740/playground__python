"""
This type stub file was generated by pyright.
"""

def get_template(template_name, using=...):
    """
    Load and return a template for the given name.

    Raise TemplateDoesNotExist if no such template exists.
    """
    ...

def select_template(template_name_list, using=...):
    """
    Load and return a template for one of the given names.

    Try names in order and return the first template found.

    Raise TemplateDoesNotExist if no such template exists.
    """
    ...

def render_to_string(template_name, context=..., request=..., using=...):
    """
    Load a template and render it with a context. Return a string.

    template_name may be a string or a list of strings.
    """
    ...

