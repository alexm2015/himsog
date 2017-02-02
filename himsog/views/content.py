from django.core.files.base import File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from himsog.forms.content import ContentForm
from himsog.models import Content, ContentImage


class ContentView(View):
    """
    """

    context = {}

    def get(self, request, content_id):
        """
        """


        content = get_object_or_404(Content, pk=content_id)
        primary_image = content.images.filter(is_primary=True).order_by('id')[0]

        self.context['content'] = content
        self.context['primary_image'] = primary_image

        return render(request,
                      'content.html',
                      self.context)


class ContentAddView(View):
    """
    """

    context = {}

    def get(self, request):
        """
        """

        content_form = ContentForm()
        self.context['form'] = content_form

        return render(request,
                      'content_add.html',
                      self.context)

    def post(self, request):
        """
        """

        content_form = ContentForm(request.POST, request.FILES)

        if not content_form.is_valid():
            # return error
            pass

        content_form.clean()
        content = Content()
        content.category = content_form.cleaned_data.get('category')
        content.title = content_form.cleaned_data.get('title')
        content.description = content_form.cleaned_data.get('description')

        img_up = content_form.cleaned_data.get('images')
        img_temp = NamedTemporaryFile(delete=True)
        for chunk in img_up.chunks():
            img_temp.write(chunk)

        content_image = ContentImage()
        content_image.image = File(img_temp)
        content_image.name = img_up.name
        content_image.save()

        content.save()

        content.images.add(content_image)

        content.save()


        self.context['content'] = content
        self.context['image_count'] = range(content.images.count())

        return render(request,
                      'content.html',
                      self.context)

class ContentUpdateView(View):
    pass

class ContentDeleteView(View):
    pass
