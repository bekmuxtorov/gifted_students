from django import template


register = template.Library()

@register.filter(name="dot_reverse")
def dot_reverse(value):
    return value.replace(",", ".")