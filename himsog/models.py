from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=256)
    slug_name = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class ContentImage(models.Model):

    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images')


class Content(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256)
    description = models.TextField()
    images = models.ManyToManyField(ContentImage)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Content, self).save(*args, **kwargs)
