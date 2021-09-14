"""
This type stub file was generated by pyright.
"""

from django.utils.functional import cached_property
from django.utils.html import html_safe

@html_safe
class BoundField:
    "A Field plus data"
    def __init__(self, form, field, name) -> None:
        ...
    
    def __str__(self) -> str:
        """Render this field as an HTML widget."""
        ...
    
    @cached_property
    def subwidgets(self):
        """
        Most widgets yield a single subwidget, but others like RadioSelect and
        CheckboxSelectMultiple produce one subwidget for each choice.

        This property is cached so that only one database query occurs when
        rendering ModelChoiceFields.
        """
        ...
    
    def __bool__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def __getitem__(self, idx):
        ...
    
    @property
    def errors(self):
        """
        Return an ErrorList (empty if there are no errors) for this field.
        """
        ...
    
    def as_widget(self, widget=..., attrs=..., only_initial=...):
        """
        Render the field by rendering the passed widget, adding any HTML
        attributes passed as attrs. If a widget isn't specified, use the
        field's default widget.
        """
        ...
    
    def as_text(self, attrs=..., **kwargs):
        """
        Return a string of HTML for representing this as an <input type="text">.
        """
        ...
    
    def as_textarea(self, attrs=..., **kwargs):
        """Return a string of HTML for representing this as a <textarea>."""
        ...
    
    def as_hidden(self, attrs=..., **kwargs):
        """
        Return a string of HTML for representing this as an <input type="hidden">.
        """
        ...
    
    @property
    def data(self):
        """
        Return the data for this BoundField, or None if it wasn't given.
        """
        ...
    
    def value(self):
        """
        Return the value for this BoundField, using the initial value if
        the form is not bound or the data otherwise.
        """
        ...
    
    def label_tag(self, contents=..., attrs=..., label_suffix=...):
        """
        Wrap the given contents in a <label>, if the field has an ID attribute.
        contents should be mark_safe'd to avoid HTML escaping. If contents
        aren't given, use the field's HTML-escaped label.

        If attrs are given, use them as HTML attributes on the <label> tag.

        label_suffix overrides the form's label_suffix.
        """
        ...
    
    def css_classes(self, extra_classes=...):
        """
        Return a string of space-separated CSS classes for this field.
        """
        ...
    
    @property
    def is_hidden(self):
        """Return True if this BoundField's widget is hidden."""
        ...
    
    @property
    def auto_id(self):
        """
        Calculate and return the ID attribute for this BoundField, if the
        associated Form has specified auto_id. Return an empty string otherwise.
        """
        ...
    
    @property
    def id_for_label(self):
        """
        Wrapper around the field widget's `id_for_label` method.
        Useful, for example, for focusing on this field regardless of whether
        it has a single widget or a MultiWidget.
        """
        ...
    
    @cached_property
    def initial(self):
        ...
    
    def build_widget_attrs(self, attrs, widget=...):
        ...
    
    @property
    def widget_type(self):
        ...
    


@html_safe
class BoundWidget:
    """
    A container class used for iterating over widgets. This is useful for
    widgets that have choices. For example, the following can be used in a
    template:

    {% for radio in myform.beatles %}
      <label for="{{ radio.id_for_label }}">
        {{ radio.choice_label }}
        <span class="radio">{{ radio.tag }}</span>
      </label>
    {% endfor %}
    """
    def __init__(self, parent_widget, data, renderer) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def tag(self, wrap_label=...):
        ...
    
    @property
    def template_name(self):
        ...
    
    @property
    def id_for_label(self):
        ...
    
    @property
    def choice_label(self):
        ...
    


