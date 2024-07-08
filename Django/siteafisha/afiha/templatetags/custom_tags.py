from afiha.utils import menu
from django import template

register = template.Library()

@register.simple_tag
def get_menu():
    return menu
