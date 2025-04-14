from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    """Subtrai o argumento do valor"""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def percentage(value, total):
    """Calcula a porcentagem de value em relação ao total"""
    try:
        if float(total) == 0:
            return 0
        return (float(value) / float(total)) * 100
    except (ValueError, TypeError):
        return 0 