import os
import random

from django.core.files.base import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from sampledatahelper.helper import SampleDataHelper

from himsog.models import Category, Content, Comment, ContentImage
from settings.settings import BASE_DIR


class Command(BaseCommand):
    """
    """

    args = ''
    help = 'Populates database with sample data'
    sdh = SampleDataHelper(seed=1234567890)


    def generate_content(self, category, instances, comments=0, images=0):

        for _ in range(instances):
            content = Content.objects.create(category=category,
                                             title=self.sdh.words(1, 10),
                                             description=self.sdh.paragraphs())
            content.views = self.sdh.int()
            content.rating = self.sdh.float(min_value=0, max_value=5)

            for _ in range(random.randint(0, images)):
                content_image = ContentImage.objects.create(name=self.sdh.words())
                data = self.sdh.image(800, 600, typ='random')

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(data.read())

                content_image.image = File(img_temp)
                content_image.save()

                content.images.add(content_image)

            for _ in range(random.randint(0, comments)):
                comment = Comment.objects.create(comment=self.sdh.words(1, 250))
                content.comments.add(comment)

            content.save()

    def handle(self, *args, **options):

        print('Populating database')

        category_food, _ = Category.objects.get_or_create(name='Food And Supplements')
        self.generate_content(category_food, instances=20, comments=10, images=4)

        category_service, _ = Category.objects.get_or_create(name='Services')
        self.generate_content(category_service, instances=25, comments=10, images=3)

        category_event, _ = Category.objects.get_or_create(name='Events')
        self.generate_content(category_event, instances=10, comments=10, images=10)

        category_article, _ = Category.objects.get_or_create(name='Articles')
        self.generate_content(category_article, instances=30, comments=10, images=2)

        print('Database population complete')
