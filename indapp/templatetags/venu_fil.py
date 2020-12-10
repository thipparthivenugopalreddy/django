from django import template

register=template.Library()

@register.filter(name='m')
def mani(value):
    x=value.split('_')
    return x[0]
