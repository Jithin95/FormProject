from django import template
from django.forms import CheckboxInput, RadioSelect

register = template.Library()

#register.filter('is_checkbox', is_checkbox)
#@register.filter
@register.filter(name= 'is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__ == RadioSelect().__class__.__name__
