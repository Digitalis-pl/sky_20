from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def only_100(some_str):
    text = some_str.split()
    return f'{" ".join(text[:40])}...'

