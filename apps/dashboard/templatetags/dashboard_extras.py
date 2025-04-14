from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    """Calcula a variação percentual entre dois valores"""
    try:
        return ((float(value) - float(arg)) / float(arg)) * 100
    except (ValueError, ZeroDivisionError, TypeError):
        return 0 