import random

from django.core.management.base import BaseCommand
from sampledatahelper.helper import SampleDataHelper

from himsog.models import Category
from himsog.models import Content
from himsog.models import ContentImage


class Command(BaseCommand):
    """
    """

    args = ''
    help = 'Populates database with sample data'
    sdh = SampleDataHelper(seed=1234567890)


    def generate_content(self, category, instances, images=0):

        for _ in range(instances):
            content = Content.objects.create(category=category,
                                             title=self.sdh.words(1, 10),
                                             content1=self.sdh.long_sentence(),
                                             content2=self.sdh.long_sentence(),
                                             content3=self.sdh.long_sentence())
            content.views = self.sdh.int()
            content.rating = self.sdh.float(min_value=0, max_value=5)

            for x in range(random.randint(0, images)):

                is_primary = False
                if x == 1:
                    is_primary = True

                url = 'http://placehold.it/1920x1080'
                content_image = ContentImage.objects.create(name=self.sdh.words(),
                                                            url=url,
                                                            is_primary=is_primary)
                content.images.add(content_image)

            content.save()

    def handle(self, *args, **options):

        print('Populating database')

        category_food, _ = Category.objects.get_or_create(name='Food And Supplements')
        self.generate_content(category_food, instances=30, images=15)

#         category_service, _ = Category.objects.get_or_create(name='Services')
#         self.generate_content(category_service, instances=2, images=5)
#
#         category_event, _ = Category.objects.get_or_create(name='Events')
#         self.generate_content(category_event, instances=2, images=10)
#
#         category_article, _ = Category.objects.get_or_create(name='Articles')
#         self.generate_content(category_article, instances=1, images=2)

        print('Database population complete')
