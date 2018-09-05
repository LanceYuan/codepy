from django import template
register = template.Library()

@register.filter(name="add_str")
def add_str(args):
    return "{0} lily is a pretty girl.".format(args)

@register.filter(name="str_args")
def str_args(obj, args):
    return "{0} {1}".format(obj, args)
