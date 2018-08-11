from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True, name='phone_filter')
def phone_filter(value):
    if len(value) > 10:
        return '(%s) %s-%s' % (value[0:2], value[2:7], value[7:])
    else:
        return '(%s) %s-%s' % (value[0:2], value[2:6], value[6:])

@register.filter(is_safe=True, name='cep_filter')
def cep_filter(value):
    return '%s-%s' % (value[0:5], value[5:])