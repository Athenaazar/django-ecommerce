from django import template

register = template.Library()


@register.filter(name='featured')
def featured(things):
    return things.filter(is_featured=True)


@register.filter(name='hot')
def hot(things):
    return things.filter(tag='out-of-stock')
