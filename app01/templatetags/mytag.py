from django import template
from app01.models import Book

register = template.Library()

@register.simple_tag
def get_book(num=3):
    return Book.objects.all()[:num]
