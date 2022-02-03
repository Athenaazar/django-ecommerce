from django import template

register = template.Library()


@register.filter(name='featured')
def featured(things):
    return things.filter(is_featured=True)


