from django import template

from himsog.models import Category
from himsog.models import Content

register = template.Library()

@register.assignment_tag
def all_categories():
    '''
    Get all available categories and its count
    '''

    __ALL__ = 'All'

    context_list = list()
    categories = Category.objects.all()

    # First item in list
    context_list.append({'category' : {'name' : __ALL__,
                                       'slug_name' : None},
                         'count' : Content.objects.all().count()})

    for category in categories:
        category_dict = dict()
        category_dict['category'] = category
        category_dict['count'] = Content.objects.filter(category=category).count()
        context_list.append(category_dict)

    return context_list
