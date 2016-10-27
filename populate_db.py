import os

import django
from django.utils import lorem_ipsum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

from himsog.models import Category
from himsog.models import Comment
from himsog.models import Content


def add_content(category, title, description):
    """
    Add a new content or update description of existing content in the database
    """

    content, _ = Content.objects.get_or_create(category=category,
                                               title=title)
    content.description = description
    content.save()
    return content

def add_comment(content, comment, comment_type=1):
    comment, _ = Comment.objects.get_or_create(comment=comment,
                                               comment_type=comment_type)
    content.comments.add(comment)


def populate_db():
    """
    Adds mock data into the database
    """

    # create categories
    category_food, _ = Category.objects.get_or_create(name='Food And Supplements')
    category_service, _ = Category.objects.get_or_create(name='Services')
    category_event, _ = Category.objects.get_or_create(name='Events')
    category_article, _ = Category.objects.get_or_create(name='Articles')

    ### add events ###
    content = add_content(category=category_event,
                          title='Event 1',
                          description=lorem_ipsum.paragraph())
    # remove all existing comments
    content.comments.all().delete()

    # add new comments
    add_comment(content=content,
                comment='Comment A')
    add_comment(content=content,
                comment='Comment B')

    ### add articles###
    content = add_content(category=category_article,
                          title='Article 1',
                          description='\n'.join(lorem_ipsum.paragraphs(2)))

    # remove all existing comments
    content.comments.all().delete()

    # add new comments
    add_comment(content=content,
                comment='Comment 1')
    add_comment(content=content,
                comment='Comment 2')
    add_comment(content=content,
                comment='Comment 3')

    content = add_content(category=category_article,
                          title='Article 2',
                          description='\n'.join(lorem_ipsum.paragraphs(3)))

    # remove all existing comments
    content.comments.all().delete()

    # add new comments
    add_comment(content=content,
                comment='Comment 4')
    add_comment(content=content,
                comment='Comment 5')


if __name__ == '__main__':
    populate_db()


