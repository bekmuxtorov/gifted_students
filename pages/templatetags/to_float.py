from django import template

register = template.Library()

@register.filter(name='to_float')
def to_float(value):
    print(value)
    return float(value)