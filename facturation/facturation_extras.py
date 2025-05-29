# facturation/templatetags/facturation_extras.py
from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Multiplie la valeur par l'argument.
    Utilisation: {{ value|mul:arg }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return '' # Ou une gestion d'erreur plus appropriée

@register.filter
def div(value, arg):
    """
    Divise la valeur par l'argument.
    Utilisation: {{ value|div:arg }}
    """
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return '' # Ou une gestion d'erreur plus appropriée