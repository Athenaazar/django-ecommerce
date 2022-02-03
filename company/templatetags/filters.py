from django import template

register = template.Library()


@register.filter(name='product_featured')
def product_featured(things):
    return things.filter(is_featured=True)
