from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    name = models.CharField(max_length=256)
    slug_name = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug_name = slugify
        super(Category, self).save(*args, **kwargs)


class Comment(models.Model):

    comment = models.TextField()
    type = models.IntegerField()


class ContentImage(models.Model):

    name = models.CharField(max_length=256)
    image = models.ImageField()
    rating = models.IntegerField()
    comments = models.ManyToManyField(Comment)


class Content(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256)
    description = models.TextField()
    images = models.ManyToManyField(ContentImage)
    comments = models.ManyToManyField(Comment)
