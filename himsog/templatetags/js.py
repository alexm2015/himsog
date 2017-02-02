from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def get_image_urls(content):

    image_urls = []
    for image in content.images.all():
        image_urls.append(image.url)

    return mark_safe(image_urls)
