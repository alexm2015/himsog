from django import template

from himsog.models import Category


register = template.Library()

@register.assignment_tag
def all_categories():
    """
    Get all available categories
    """

    return Category.objects.all()

