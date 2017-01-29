from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """
    Content category model
    """

    name = models.CharField(max_length=256)
    slug_name = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

class ContentImage(models.Model):
    """
    Content image model
    """

    name = models.CharField(max_length=256)
    url = models.URLField()
    is_primary = models.BooleanField(default=False)


class Content(models.Model):
    """
    Content model
    """

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField(ContentImage)
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#
#         if not self.id:
#             self.created = timezone.now()
#
#         self.modified = timezone.now()
#         return super(Content, self).save(*args, **kwargs)
