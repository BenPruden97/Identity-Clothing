from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_subtotal_sale')
def calc_subtotal_sale(get_sale_price, quantity):
    return get_sale_price * quantity
