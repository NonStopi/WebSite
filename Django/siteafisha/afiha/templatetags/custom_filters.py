from django import template

register = template.Library()

@register.filter
def month_name(month_number):
    try:
        month_number = int(month_number)
    except ValueError:
        return ""
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    return months[month_number - 1]