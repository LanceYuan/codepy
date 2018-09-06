from django import template
from app01.models import Book

register = template.Library()

@register.simple_tag
def get_book(num=3):
    return Book.objects.all()[:num]


@register.simple_tag(name="addsum")
def add_sum(*args):
    ret = ""
    for item in args:
        ret = ret + item
    return ret
