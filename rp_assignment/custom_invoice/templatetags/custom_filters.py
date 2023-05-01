from django import template

register = template.Library()

# these are custom filters
# incorporated because parsing does not work in inline html

@register.filter
def split_lines(value):
    return value.split('\n')

@register.filter
def split_line_0(value):
    return value.split(',')[0]

@register.filter
def split_line_1(value):
    return value.split(',')[1]

@register.filter
def split_line_2(value):
    return value.split(',')[2]